# Step 3 — Parsing NotebookLM Outputs and Registering Results into the Analysis Framework
*Futures Summit 2025 Qualitative Analysis*

---

## Purpose of Step 3

Step 3 translates **narrative qualitative analysis outputs from NotebookLM** into **structured, analyzable tables** within the project’s master framework:

- `Qual_Analysis_Framework.xlsx`
- `Session_Index.csv`

This step ensures that insights generated through human-in-the-loop synthesis are:
- consistently structured,
- traceable to their analytic bucket,
- reusable for reporting, dashboards, and future planning.

Step 3 is **fully automated** and does **not** involve interpretation or new analysis.

---

## Role of Step 3 in the Overall Workflow

Step 3 sits **after qualitative reasoning is complete** and **before any reporting or dissemination**.

Conceptually, it serves as the **bridge** between:
- human-guided qualitative synthesis (NotebookLM), and
- structured analytic outputs suitable for aggregation and decision-making.

Importantly:
- Step 3 does **not care whether insights came from Pass 1 or Pass 2**
- It assumes the analyst already applied the correct *conceptual sequencing* during NotebookLM execution

---

## Inputs to Step 3

Step 3 consumes **NotebookLM response files** that have already been reviewed and approved.

### Input format

- Markdown files (`.md`)
- One file per analytic bucket
- Each file contains:
  - optional metadata header
  - a clearly delimited response block:

---BEGIN_NOTEBOOKLM_RESPONSE---

...

...
---END_NOTEBOOKLM_RESPONSE---


### Supported analytic buckets

Step 3 processes all six buckets defined in the analytic framework:

**Baseline synthesis (conceptually Pass 1):**
1. Cross_Cutting_Themes  
2. Key_Learnings  
3. Recurring_Audience_Questions  

**Diagnostic and action-oriented analysis (conceptually Pass 2):**
4. Missing_Elements  
5. Unmet_Needs  
6. Use_Cases_Exemplars  

> Note: The “pass” distinction is **conceptual only**. Step 3 operates on bucket type, not on pass labels or filenames.

---

## What Step 3 Does (Plain English)

For each NotebookLM response file, Step 3:

1. Reads the Markdown file as plain text  
2. Extracts only the content inside the BEGIN / END markers  
3. Normalizes formatting (removes Markdown artifacts such as bolding and bullets)  
4. Splits the response into individual findings using numbered items (1., 2., 3., …)  
5. Interprets labeled sections within each item (e.g., Definition, Evidence, Session IDs)  
6. Maps each item into the correct worksheet and columns in Excel  
7. Appends rows without overwriting existing data  
8. Enforces a maximum of **15 items per bucket**  
9. Records processing status in the session index  

No interpretation, summarization, or rewriting occurs in this step.

---

## Outputs of Step 3

Step 3 produces **new files** to preserve provenance and reproducibility.

### Primary outputs

- `Qual_Analysis_Framework__UPDATED_<RUN_ID>.xlsx`  
  - Contains all parsed results appended to the correct bucket sheets  
  - Preserves original template structure and definitions  

- `Session_Index__UPDATED_<RUN_ID>.csv`  
  - Records that NotebookLM outputs have been registered  
  - Tracks processing status for auditability  

Original files are **never overwritten**.

---

## Relationship to the Two-Pass Analysis Model

Step 3 is intentionally **pass-agnostic**.

The two-pass model matters for:
- analytic rigor,
- interpretive sequencing,
- defensibility of conclusions.

Step 3 assumes:
- Pass 1 synthesis was completed first
- Pass 2 diagnostics were informed by Pass 1
- outputs were reviewed before registration

Step 3’s responsibility is simply to **faithfully encode those results** into structured form.

---

## Quality Control Expectations

Before running Step 3, the analyst should confirm:

- Each NotebookLM response:
  - is complete
  - uses numbered items
  - aligns with the bucket definition
- The content reflects the intended analytic pass (baseline vs diagnostic)

After Step 3 execution, spot checks should confirm:

- Rows appear in the correct worksheet
- Key columns are populated
- No bucket exceeds 15 rows
- Metadata fields (e.g., Last Updated, Analyst Notes) are filled

---

## Exit Criteria for Step 3

Step 3 is complete when:

- All six analytic buckets are registered into Excel
- Session index reflects successful processing
- The framework is ready for:
  - synthesis across buckets
  - reporting
  - visualization
  - future programming decisions

---

## What Step 3 Does *Not* Do

- It does not generate new insights  
- It does not modify NotebookLM outputs  
- It does not evaluate quality or correctness  
- It does not enforce pass sequencing  

Those responsibilities belong to earlier steps and human review.

---
