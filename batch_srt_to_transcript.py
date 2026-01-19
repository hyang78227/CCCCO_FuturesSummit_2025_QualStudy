import os
import re
import csv
from pathlib import Path
from datetime import datetime

from google import genai

# -----------------------------
# CONFIG
# -----------------------------
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")  # fast + cheap; change if you prefer
PROJECT_ROOT = Path(__file__).resolve().parent
SRT_DIR = PROJECT_ROOT / "01_SRT_Raw"
OUT_DIR = PROJECT_ROOT / "02_Transcripts_Clean"
LOG_PATH = PROJECT_ROOT / "03_NotebookLM_Exports" / "transcript_conversion_log.csv"

OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

PROMPT = """Convert the following .srt captions file into a clean, readable transcript.

Requirements:
1) Remove all caption numbers and timestamps.
2) Remove non-speech markers such as [applause], [laughter], [music], [inaudible], [crosstalk].
3) Retain speaker information each time the speaker changes.
   - If names are not explicit, assign consistent labels such as Moderator, Panelist 1, Panelist 2, Audience.
4) Format into natural paragraphs, where each paragraph represents a complete thought or response.
5) Clearly label audience questions (e.g., "Audience Question:").
6) Do NOT summarize, rewrite, or add content.
7) Output only the transcript text.

Here is the captions file content:
"""

# -----------------------------
# HELPERS
# -----------------------------
def is_clean_enough(text: str) -> list[str]:
    """Return a list of QA issues found in the output."""
    issues = []
    if "-->" in text:
        issues.append("Found timestamp arrow '-->' (timestamps not fully removed).")
    if re.search(r"\b\d{2}:\d{2}:\d{2}[,.]\d{3}\b", text):
        issues.append("Found timestamp-like pattern (00:00:00,000).")
    if re.search(r"^\s*\d+\s*$", text, flags=re.MULTILINE):
        issues.append("Found standalone caption numbers.")
    return issues

def safe_stem_from_filename(name: str) -> str:
    # FS01_AI_Governance_captions.srt -> FS01_AI_Governance
    stem = Path(name).stem
    stem = stem.replace("_captions", "")
    return stem

# -----------------------------
# MAIN
# -----------------------------
def main():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY (or GOOGLE_API_KEY). Set it and reopen your terminal.")

    client = genai.Client(api_key=api_key)

    srt_files = sorted(SRT_DIR.glob("*.srt"))
    if not srt_files:
        print(f"No .srt files found in: {SRT_DIR}")
        return

    # Prepare log CSV (append mode)
    new_file = not LOG_PATH.exists()
    with open(LOG_PATH, "a", newline="", encoding="utf-8") as f_log:
        writer = csv.writer(f_log)
        if new_file:
            writer.writerow(["timestamp", "srt_file", "output_file", "model", "status", "qa_issues"])

        for srt_path in srt_files:
            srt_text = srt_path.read_text(encoding="utf-8", errors="ignore")
            prompt = PROMPT + "\n\n" + srt_text

            out_stem = safe_stem_from_filename(srt_path.name)
            out_path = OUT_DIR / f"{out_stem}_transcript.txt"

            try:
                resp = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                )
                transcript = (resp.text or "").strip()

                qa_issues = is_clean_enough(transcript)
                status = "OK" if not qa_issues else "QA_WARN"

                out_path.write_text(transcript + "\n", encoding="utf-8")

                writer.writerow([
                    datetime.now().isoformat(timespec="seconds"),
                    str(srt_path.name),
                    str(out_path.name),
                    MODEL,
                    status,
                    " | ".join(qa_issues)
                ])
                print(f"[{status}] {srt_path.name} -> {out_path.name}")

            except Exception as e:
                writer.writerow([
                    datetime.now().isoformat(timespec="seconds"),
                    str(srt_path.name),
                    "",
                    MODEL,
                    "ERROR",
                    str(e)
                ])
                print(f"[ERROR] {srt_path.name}: {e}")

if __name__ == "__main__":
    main()
