# AI Survey Dashboard: Text Box Summaries for Each Page

## Instructions
Copy each text box summary below and paste it into a Power BI text box on the corresponding dashboard page. These summaries are concise (60-80 words) and map directly to the survey questions.

---

## PAGE 1: AI Impact (Current/Future/Education)

**Survey Questions:**
- "How much of an impact is AI currently having on your work?"
- "To what extent do you see AI impacting your work in the future?"
- "AI's impact on education and student learning will be:"

**Text Box Summary (Copy This):**
```
This page examines AI's impact across three dimensions: current workplace impact, 
anticipated future impact, and expected effects on education and student learning. 
Use the Impact filter to toggle between these three perspectives. Data is 
disaggregated by district, with filters available for role and functional area. 
Mean scores are centered on a Likert scale (-2 to +2), where negative values 
indicate lower impact/concern and positive values indicate higher impact/optimism.
```

---

## PAGE 2: AI Use Frequency

**Survey Question:**
- "How often do you use AI tools? (e.g., ChatGPT, Co-Pilot, Bard/Gemini, Grammarly, DALL-E)"

**Text Box Summary (Copy This):**
```
This page tracks how frequently community college professionals use AI tools in 
their daily work. The state mean of -0.86 indicates usage below weekly frequency 
on average. The distribution table shows that most users fall into "Less than once 
a week" or "Weekly" categories, with significant variation across districts. This 
baseline measure helps contextualize adoption patterns and training needs.
```

---

## PAGE 3: AI Familiarity

**Survey Question:**
- "How familiar are you with the capabilities of AI?"

**Text Box Summary (Copy This):**
```
This page measures respondents' self-reported familiarity with AI capabilities. 
The state average of -0.15 suggests moderate familiarity overall, with most 
respondents reporting "Moderately familiar" or "Slightly familiar." Familiarity 
levels vary by district and role, providing insights into where targeted education 
and training resources may be most beneficial.
```

---

## PAGE 4: AI Concerns

**Survey Question:**
- "Please indicate your level of concern about the following issues related to the use of AI in education:"
  - Academic integrity
  - Information trustworthiness
  - AI bias
  - Access and equity

**Text Box Summary (Copy This):**
```
This page aggregates concern levels across four key ethical and practical issues: 
academic integrity, information trustworthiness, AI bias, and access/equity. 
The mean concern score of 0.38 indicates moderate concern overall. Use the Concern 
Issue filter to examine each topic separately. The majority of respondents express 
"Somewhat concerned" or "Extremely concerned" across all four dimensions.
```

---

## PAGE 5: AI Impact Theme

**Survey Question:**
- "In what ways might AI impact the learning experience in a community college setting?" (Open-ended)

**Text Box Summary (Copy This):**
```
This page analyzes 618 open-ended responses using semantic theme analysis. 
Responses cluster into five MainThemes: Learning & Pedagogy (42%), Risks/Integrity 
(38%), Student Experience (11%), Uncategorized (5%), and Institutional Readiness 
(4%). SubThemes provide granular insights, with Academic Integrity (122 mentions) 
and Teaching & Curriculum (70 mentions) as top concerns. Use the SubTheme filter 
to explore specific topics.
```

---

## PAGE 6: AI Use Cases

**Survey Question:**
- "How have you used AI in your work and personal life? Select all that apply"

**Text Box Summary (Copy This):**
```
This page reveals how respondents currently apply AI tools. The top three use cases 
are: drafting correspondence (48%), research (37%), and course content creation (28%). 
The disaggregation table shows variation by role—for example, student workers 
prioritize transcription/meetings and research, while faculty focus on research, 
correspondence, and course content. This data informs relevant training and support.
```

---

## PAGE 7: Training Interests

**Survey Question:**
- "What topics of instruction regarding AI would be of the most interest to you?"

**Text Box Summary (Copy This):**
```
This page identifies professional development priorities. Responsible & Ethical AI 
instruction is overwhelmingly the top interest (99%), followed distantly by AI for 
Student Services (3%) and AI for Teaching Support (1%). The role-based breakdown 
shows universal interest in ethical AI across all positions, highlighting a shared 
priority for understanding AI's responsible implementation in education.
```

---

## PAGE 8: Methodology

**Survey Question:**
- Not applicable (technical documentation)

**Text Box Summary (Copy This):**
```
This page documents the data pipeline used to process survey responses and construct 
this dashboard. Key steps include: data standardization, dimensional modeling, fact 
table construction for quantitative measures, and a dedicated semantic analysis 
pipeline for open-ended responses. The two-layer theme framework (MainThemes and 
SubThemes) enables nuanced exploration of qualitative insights while maintaining 
analytical rigor.
```

---

## QUICK REFERENCE: Survey Question Mapping

| Dashboard Page | Survey Question | Survey Page # |
|----------------|----------------|---------------|
| AI Impact | Current impact / Future impact / Education impact | Page 3 |
| AI Use Frequency | How often do you use AI tools? | Page 2 |
| AI Familiarity | How familiar are you with AI capabilities? | Page 2 |
| AI Concerns | Level of concern (4 sub-questions) | Page 3 |
| AI Impact Theme | How might AI impact learning? (open-ended) | Page 3 |
| AI Use Cases | How have you used AI? (select all) | Page 2 |
| Training Interests | What training topics interest you? | Page 4 |
| Methodology | Technical documentation | N/A |

---

## Power BI Text Box Tips

1. **Placement**: Add text box at the top of each page, below the page title
2. **Formatting**: 
   - Font size: 11-12pt for readability
   - Background: Light gray or white with subtle border
   - Padding: Add 10-15px padding inside the text box
3. **Keep it visible**: Don't let text box overlap with visualizations
4. **Character limits**: Each summary is 300-450 characters to fit standard text boxes

---

## How to Use in Power BI

**Step 1:** Open your Power BI dashboard in Edit mode

**Step 2:** Navigate to the page you want to add a summary to

**Step 3:** Insert → Text box

**Step 4:** Copy the corresponding summary from this document

**Step 5:** Paste into the text box

**Step 6:** Format:
   - Adjust size and position (place below page title)
   - Set background color (light gray: #F7F9FB works well)
   - Add border if desired
   - Center or left-align text based on your layout

**Step 7:** Repeat for all pages

---

## For the Overview Page

**Option A - Use the PowerPoint Slide:**
1. Open the PowerPoint file (AI_Survey_Dashboard_Overview.pptx)
2. Save the slide as an image (File → Export → PNG)
3. In Power BI: Insert → Image → Upload the PNG
4. Resize to fit your page

**Option B - Recreate in Power BI:**
Use the PowerPoint as a design reference and manually build it in Power BI using:
- Text boxes for content
- Card visuals for the three metrics (618, Multiple, 2/4/26)
- Buttons or shapes for the navigation boxes
- Match the teal color scheme (#028090)
