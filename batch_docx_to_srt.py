from pathlib import Path
import re
from docx import Document

# ============================================================
# YOUR EXACT FOLDERS
# ============================================================
INPUT_DIR = Path(
    r"C:\Users\hyang\Documents\FuturesSummit_2025_QualStudy\2025 Futures Captions_word"
)

OUTPUT_DIR = Path(
    r"C:\Users\hyang\Documents\FuturesSummit_2025_QualStudy\01_SRT_Raw"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Match SRT timestamp lines
TIMESTAMP_RE = re.compile(
    r"^\d\d:\d\d:\d\d[,.]\d+\s-->\s\d\d:\d\d:\d\d[,.]\d+$"
)

def extract_lines_from_docx(docx_path: Path):
    doc = Document(str(docx_path))
    lines = []
    for p in doc.paragraphs:
        t = (p.text or "").strip()
        if t:
            lines.append(t)
    return lines

def normalize_timestamp(ts: str) -> str:
    # SRT standard uses commas for milliseconds
    return ts.replace(".", ",")

def write_srt(lines, srt_path: Path):
    out = []
    idx = 1
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip numeric-only lines (old caption numbering)
        if line.isdigit():
            i += 1
            continue

        # Timestamp line
        ts_candidate = line.replace(".", ",")
        if TIMESTAMP_RE.match(ts_candidate):
            out.append(str(idx))
            out.append(normalize_timestamp(line))
            idx += 1
            i += 1

            text_buf = []
            while i < len(lines):
                nxt = lines[i]
                nxt_ts = nxt.replace(".", ",")
                if nxt.isdigit():
                    i += 1
                    continue
                if TIMESTAMP_RE.match(nxt_ts):
                    break
                text_buf.append(nxt)
                i += 1

            out.append(" ".join(text_buf).strip())
            out.append("")  # blank line between SRT blocks
        else:
            i += 1

    srt_path.write_text("\n".join(out).strip() + "\n", encoding="utf-8")

def main():
    docx_files = sorted(INPUT_DIR.glob("*.docx"))
    if not docx_files:
        print(f"No .docx files found in: {INPUT_DIR}")
        return

    for docx_path in docx_files:
        srt_path = OUTPUT_DIR / f"{docx_path.stem}.srt"
        lines = extract_lines_from_docx(docx_path)
        write_srt(lines, srt_path)
        print(f"Created SRT: {srt_path.name}")

if __name__ == "__main__":
    main()
