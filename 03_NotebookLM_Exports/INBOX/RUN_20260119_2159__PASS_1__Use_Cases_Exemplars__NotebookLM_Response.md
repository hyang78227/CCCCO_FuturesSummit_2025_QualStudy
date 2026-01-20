RUN_ID: RUN_20260119_2159
PASS_ID: PASS_1
BUCKET: Use_Cases_Exemplars
NOTEBOOK: FuturesSummit_2025_Qual_Analysis_AllSessions
DATE: 2026-01-19
ANALYST: Hongling
SOURCE_SET: All transcripts in 02_Transcripts_Clean
---BEGIN_NOTEBOOKLM_RESPONSE---

Based on the session transcripts, here are the identified use cases and exemplars of AI implementation.

### **Use Cases Identified**

1.  **24/7 Multilingual Tech Support Bot**
    *   **Who is using AI:** IT Department at Mendocino College.
    *   **Context and Purpose:** The college faced an "explosion of tickets" for password resets and Wi-Fi access at the start of semesters and lacked staff to cover overnight hours or support Spanish-speaking students effectively. They implemented a bot via Invoke Learning.
    *   **Benefits or Outcomes:** The bot handles password resets via API, integrates with the ticketing system, and speaks Spanish (which only one human staff member could do). It resulted in a noticeable drop in tier-one calls, described as "a little quiet, a little bit eerie" for staff.
    *   **Risks or Constraints:** None explicitly mentioned as a negative, though they had to iterate to find a Spanish voice that didn't sound like a "Swedish person speaking Spanish."
    *   **Session_ID and Speaker:** Cam A Session 1 v1(1), Dave Johnston (CTO).
    *   **Supporting Quotes:** "It can do password resets for students... The folks that normally handle those tier-one phone calls... It's been a little quiet, a little bit eerie, for them."

2.  **Admissions Fraud Detection (LightLeap)**
    *   **Who is using AI:** Admissions & Records and IT Departments across 83 California Community Colleges (including Foothill-De Anza).
    *   **Context and Purpose:** Colleges faced a massive surge in fraudulent applications (bots applying for financial aid). Legacy models were insufficient.
    *   **Benefits or Outcomes:** The system processed 3 million applications and identified 850,000 fraudulent actors. In a side-by-side test with legacy models, the AI discovered "double the amount" of fraud. San Bernardino saw a drop in fraud from 30% to 7%.
    *   **Risks or Constraints:** Requires historical data to train the model effectively.
    *   **Session_ID and Speaker:** Cam A Session 1 v1(1), Jory Hadsell; General Session Opening Session Day 2, Kiran Kodithala.
    *   **Supporting Quotes:** "We ran it side by side with our in-house-developed legacy fraud model and we actually discovered double the amount of what we thought we had."; "We caught close to 850,000 fraudulent factors."

3.  **Student Program Eligibility Assessment**
    *   **Who is using AI:** Student Services Advisors at West Valley-Mission Community College District.
    *   **Context and Purpose:** Students had to fill out multiple forms for different support programs (EOPS, TRIO, MESA). Data was siloed in different systems (CCApply, Banner).
    *   **Benefits or Outcomes:** An AI model was trained on program criteria to scan student data and flag eligibility automatically. This saved advisors approximately five hours a week, with a projected savings of 3,000 staff hours a year, allowing them to focus on outreach.
    *   **Risks or Constraints:** Advisors still perform a "human assessment" to verify the AI's findings.
    *   **Session_ID and Speaker:** Cam A Session 1 v1(1), Joel Bennett & Amanda Marshall.
    *   **Supporting Quotes:** "We trained AI to assess student data and determine whether they're eligible... This is saving her five hours a week."

4.  **Digitization of Incarcerated Student Applications**
    *   **Who is using AI:** Admissions staff at Palo Verde College.
    *   **Context and Purpose:** The college serves incarcerated students and fire science students who lack internet access and must use paper applications. Manual entry was time-consuming and prone to error due to bad handwriting.
    *   **Benefits or Outcomes:** Applications are scanned, and AI extracts handwritten data directly into the Student Information System (SIS). It includes an accuracy meter (e.g., 90% accurate). The process was described as "night and day" for staff efficiency.
    *   **Risks or Constraints:** Staff must double-check data if the accuracy confidence score is low (below 80-85%).
    *   **Session_ID and Speaker:** Cam A Session 1 v1(1), Ger Xiong.
    *   **Supporting Quotes:** "They then extract these handwritten data into our SIS system directly... finding N2N as a solution to process this has been night and day for us.",

5.  **Project Greenlight: Traffic Optimization**
    *   **Who is using AI:** City Traffic Engineers (using Google AI).
    *   **Context and Purpose:** Reducing "stop-and-go" traffic at intersections, which causes 29 times higher pollution than open roads. Engineers typically only retime lights every five years.
    *   **Benefits or Outcomes:** AI uses driving trends to suggest small timing changes. This resulted in up to 30% reduction in stop-and-go traffic and 10% reduction in emissions in cities like Boston and Rio de Janeiro.
    *   **Risks or Constraints:** None explicitly mentioned.
    *   **Session_ID and Speaker:** Cam C Session 4 v1, Juliet Rothenberg.
    *   **Supporting Quotes:** "Traffic engineers are able to change an intersection in a matter of minutes, and we've seen up to 30% reduction in stop-and-go traffic."

6.  **Contrail Prediction for Aviation**
    *   **Who is using AI:** Pilots and Air Traffic Control (e.g., American Airlines, EU Eurocontrol).
    *   **Context and Purpose:** Contrails (clouds formed by planes) trap heat and account for 1/3 of aviation's global warming impact.
    *   **Benefits or Outcomes:** AI predicts where contrails will form based on satellite imagery and weather data. Pilots adjust altitude slightly to avoid these zones, reducing contrails by over 50%.
    *   **Risks or Constraints:** None explicitly mentioned.
    *   **Session_ID and Speaker:** Cam C Session 4 v1, Juliet Rothenberg.
    *   **Supporting Quotes:** "We've used AI to predict where contrails will form and had pilots in live flights adjust the altitude... they've reduced contrails by over 50%."

7.  **Automated Alt-Text Generation for Accessibility**
    *   **Who is using AI:** Interns/Developers at Amazon (Jessica Lopez).
    *   **Context and Purpose:** A project to make Amazon's internship application pages accessible for students with disabilities revealed a lack of alt-text on images, creating barriers for screen readers.
    *   **Benefits or Outcomes:** An AI agent was used to generate image descriptions. A process estimated to take four months was completed in one week.
    *   **Risks or Constraints:** Requires auditing to ensure accuracy, as AI can hallucinate or lack context.
    *   **Session_ID and Speaker:** Cam A Session 4 v1(1), Jessica Lopez.
    *   **Supporting Quotes:** "What ended up being originally estimated as a four month process ended up taking a week. This is the power of accessibility and using AI."

8.  **"Nectar" Bot for Syllabus and Nursing Scenarios**
    *   **Who is using AI:** Nursing and Child Development Faculty at Cerro Coso Community College.
    *   **Context and Purpose:** To answer repetitive student questions (due dates, APA formatting) and to run clinical simulations where the bot plays a patient/scenario role.
    *   **Benefits or Outcomes:** Handled 3,500 messages for one class, reducing faculty email load ("gave me back time to teach humans"). It allows 24/7 support for students.
    *   **Risks or Constraints:** Faculty must configure "guardrails" to prevent hallucinations; the bot is trained *only* on course data (RAG) to ensure accuracy.
    *   **Session_ID and Speaker:** Cam A Session 3 v1(1), Matthew Wanta.
    *   **Supporting Quotes:** "It was one single class, 25 students, and we had over 3,500 student messages... AI gave me back time to teach humans, not chase housekeeping emails.",

9.  **Mental Health & Coping Strategy App (Flourish)**
    *   **Who is using AI:** Students (at Foothill College and others).
    *   **Context and Purpose:** Addressing student loneliness and anxiety ("yellow zone" mental health issues) using an AI companion named "Sunny" that is grounded in positive psychology.
    *   **Benefits or Outcomes:** 76% of students in a pilot preferred it over other options. It offers safety planning and proactively suggests coping strategies rather than just chatting.
    *   **Risks or Constraints:** Cannot replace therapy for high-risk ("red zone") cases; requires strict privacy/safety protocols for suicidal ideation (e.g., safety planning features).
    *   **Session_ID and Speaker:** Cam C Session 5 v1, Dr. Xuan Zhao / Alex Kraft.
    *   **Supporting Quotes:** "With AI it can actually guide people to learn coping strategies and to make better sense of what they are going through."

10. **Student-Built Shipping Optimization Tool**
    *   **Who is using AI:** Cal Poly Procurement (Student Project).
    *   **Context and Purpose:** A student team at an AI summer camp was challenged to optimize shipping methods using procurement data.
    *   **Benefits or Outcomes:** Created a chatbot ("Expedia for shipping") that checks API pricing for FedEx/UPS. Projected $15,000–$25,000 in potential savings by identifying inefficiencies (e.g., shipping six times instead of once).
    *   **Risks or Constraints:** Students noted difficulty with "messy" non-standardized data.
    *   **Session_ID and Speaker:** Cam D Session 4 v1, River Covey (Student).
    *   **Supporting Quotes:** "We projected 15 to 25,000 in potential shipping savings... All this was possible with AWS and AI tools."

***

### **Exemplars**

The following use cases stand out as exemplars based on the criteria of clarity, specificity, and impact:

**1. Admissions Fraud Detection (LightLeap)**
*   **Why it is an exemplar:**
    *   **Impact:** The scale is massive (850,000 fraudulent actors caught), directly protecting financial aid resources for real students.
    *   **Specificity:** The comparison between legacy models and the AI model (finding "double" the fraud) provides clear evidence of efficacy.
    *   **Replicability:** It has already been scaled to over 80 colleges, proving it is a systemic solution rather than a one-off pilot.

**2. Automated Alt-Text Generation (Amazon Internship Project)**
*   **Why it is an exemplar:**
    *   **Clarity & Impact:** It provides a stark "before and after" metric (4 months vs. 1 week), perfectly illustrating the efficiency gains of AI for accessibility compliance.
    *   **Replicability:** This is a specific task (image-to-text description) that every college website administrator faces, making it a highly transferable use case for higher education institutions struggling with WCAG compliance.

**3. Google’s Contrail Prediction**
*   **Why it is an exemplar:**
    *   **Impact:** It addresses a major global challenge (climate change) with a quantifiable metric (50% reduction in contrails).
    *   **Specificity:** It explains exactly *how* the AI is used (satellite imagery + weather data -> altitude adjustment), demystifying "AI for climate" into a concrete operational change.

**4. Mendocino College Tech Support Bot**
*   **Why it is an exemplar:**
    *   **Replicability:** Every college faces the "password reset" volume spike at the start of the semester.
    *   **Clarity:** The problem (small IT staff, high volume) and solution (API-connected bot) are clearly defined.
    *   **Equity:** It highlights a specific benefit for non-English speakers (Spanish support) that the human staff could not provide, showcasing how AI extends service capacity.

---END_NOTEBOOKLM_RESPONSE---
