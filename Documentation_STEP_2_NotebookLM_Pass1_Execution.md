# Step 2 — NotebookLM Analysis Execution
*Futures Summit 2025 Qualitative Analysis*

---

## Purpose of Step 2

Step 2 executes the **qualitative analysis in NotebookLM** using structured prompts derived from the analytic framework.

This step produces the **core analytic content** that will later be parsed and registered into structured tables.

---

## Two-Pass Analysis Model (Reader-Facing Explanation)

Although NotebookLM runs are executed as individual prompts, the analysis follows a **two-pass conceptual model**.

This model exists to support clarity, rigor, and defensibility of conclusions.

---

## Pass 1 — Baseline Synthesis

### What Pass 1 Is For

Pass 1 captures **what is present in the conference content**.

It focuses on synthesis rather than evaluation.

### Pass 1 Buckets

The following analytic buckets belong to Pass 1:

1. **Cross-Cutting Themes**  
   Identifies recurring patterns that span multiple sessions.

2. **Key Learnings**  
   Articulates the most important takeaways from the conference.

3. **Recurring Audience Questions**  
   Clusters questions to surface shared concerns and priorities.

### Pass 1 Guiding Question

> “What did participants collectively express, learn, and ask during the conference?”

---

## Pass 2 — Diagnostic and Action-Oriented Analysis

### What Pass 2 Is For

Pass 2 builds on the baseline established in Pass 1.

It focuses on **gaps, needs, and actionable insights** rather than summary.

### Pass 2 Buckets

The following analytic buckets belong to Pass 2:

4. **Missing Elements**  
   Identifies topics or perspectives that should have surfaced but did not.

5. **Unmet Needs**  
   Articulates stakeholder needs that remain insufficiently addressed.

6. **Use Cases / Exemplars**  
   Extracts concrete examples that can inform future sessions or materials.

### Pass 2 Guiding Question

> “Given what we heard in Pass 1, what is still missing or needed for future programming?”

---

## Important Clarification About Execution

The distinction between Pass 1 and Pass 2 is **conceptual**, not enforced by tooling.

- NotebookLM prompts are executed individually.
- File naming may not always reflect pass membership.
- Analysis correctness depends on **intent and order of reasoning**, not labels.

Readers should interpret the passes as **analytic lenses applied sequentially**, not as rigid system states.

---

## NotebookLM Execution Principles

- One NotebookLM notebook is used for all sessions.
- All transcripts are available to NotebookLM for every prompt.
- Prompts are run **one bucket at a time**.
- Outputs are reviewed for quality before registration.

This ensures:
- consistency of context,
- comparability across buckets,
- and traceability of conclusions.

---

## Step 2 Outputs

Step 2 produces:
- narrative analytic responses per bucket,
- saved as Markdown files,
- staged for structured parsing in the next step.

No structured tables are written during Step 2.

---

## Exit Criteria for Step 2

Step 2 is complete when:
- all six buckets have been analyzed,
- outputs are reviewed and accepted,
- and results are ready for structured registration.

---
