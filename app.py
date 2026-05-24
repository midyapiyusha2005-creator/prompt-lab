import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Prompt Lab",
    page_icon="📘",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background-color: #F4F6F9;
    color: #1E1E1E;
}

/* Header */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #0B3D91;
    margin-bottom: 5px;
}

.sub-title {
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}

/* Section Box */
.section-box {
    background-color: white;
    padding: 22px;
    border-radius: 12px;
    border-left: 6px solid #0B3D91;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

/* Section Title */
.section-title {
    font-size: 24px;
    font-weight: 600;
    color: #0B3D91;
    margin-bottom: 10px;
}

/* Scenario Card */
.scenario-card {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #D9E2EC;
}

/* Prompt Box */
textarea {
    border-radius: 12px !important;
    font-size: 16px !important;
    border: 1px solid #C9D6E2 !important;
    background-color: #FFFFFF !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
}
            
            /* Evaluation Box */
.eval-box {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    margin-top: 15px;
    margin-bottom: 20px;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown(
    '<div class="main-title">PROMPT LAB</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Business Prompting Simulation Environment</div>',
    unsafe_allow_html=True
)

st.caption(
    "Scenario-Based Prompt Engineering Capability Assessment"
)

# ---------------- FRAMEWORK ---------------- #
st.markdown("## Enterprise Prompting Framework — RCTCF")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("### ROLE")
    st.caption("Define expertise")

with col2:
    st.markdown("### CONTEXT")
    st.caption("Business situation")

with col3:
    st.markdown("### TASK")
    st.caption("Expected analysis")

with col4:
    st.markdown("### CONSTRAINTS")
    st.caption("Operational limitations")

with col5:
    st.markdown("### FORMAT")
    st.caption("Output structure")

st.divider()

# ---------------- SCENARIOS ---------------- #
scenarios = {

    "Scenario 1 — Safety Incident Increase in Night Shift": {

        "insight":
        "Near-miss safety incidents increased during night shifts in the Raw Materials division over the last 45 days.",

        "data": [
            "Shift timing",
            "Incident count",
            "Department",
            "Employee fatigue records",
            "Overtime hours",
            "Supervisor roster",
            "Safety audit findings"
        ],

        "objective": [
            "Root cause analysis",
            "High-risk area identification",
            "Preventive action planning"
        ],

        "task":
        """
Create a structured business prompt using the RCTCF framework.

Your prompt should:
- Use available operational data
- Define appropriate expert role
- Request analysis and recommendations
- Include practical operational constraints
- Ask for structured output
        """
    },

    "Scenario 2 — Low Adoption of Digital Tools": {

        "insight":
        "Maintenance employees are not regularly using newly launched digital inspection applications despite completing training programs.",

        "data": [
            "Training completion records",
            "Application login frequency",
            "Department-wise usage",
            "Employee feedback",
            "Device availability"
        ],

        "objective": [
            "Identify adoption barriers",
            "Improve usage engagement",
            "Increase workforce enablement"
        ],

        "task":
        """
Create a structured prompt using the RCTCF framework.

Focus on:
- Digital adoption challenges
- Workforce usability
- Practical implementation strategies
        """
    },

    "Scenario 3 — Decline in Training Engagement": {

        "insight":
        "Mandatory compliance training completion dropped from 92% to 61% among contract workforce employees.",

        "data": [
            "Training attendance",
            "Completion percentage",
            "Language preference",
            "Department-wise participation",
            "Feedback scores"
        ],

        "objective": [
            "Analyze declining engagement",
            "Identify operational challenges",
            "Recommend intervention strategies"
        ],

        "task":
        """
Develop a business-focused prompt using the RCTCF framework.

Ensure your prompt:
- Requests actionable analysis
- Includes workforce considerations
- Specifies output structure
        """
    }

,
    "Scenario 4 — High Downtime in Equipment": {

        "insight":
        "A critical conveyor system experienced repeated downtime during peak operational hours, impacting dispatch timelines and productivity.",

        "data": [
            "Equipment maintenance logs",
            "Downtime duration",
            "Breakdown frequency",
            "Maintenance schedules",
            "Operator reports",
            "Production impact data"
        ],

        "objective": [
            "Identify probable downtime causes",
            "Reduce operational disruption",
            "Improve preventive maintenance planning"
        ],

        "task":
        """
Create a structured prompt using the RCTCF framework.

Your prompt should:
- Analyze operational patterns
- Identify root causes
- Recommend preventive actions
- Focus on practical maintenance improvements
        """
    },

    "Scenario 5 — Employee Engagement Survey Drop": {

        "insight":
        "Employee engagement scores reduced significantly in one production department after shift restructuring.",

        "data": [
            "Employee survey scores",
            "Shift schedules",
            "Department feedback",
            "Attrition trends",
            "Attendance records",
            "Manager feedback"
        ],

        "objective": [
            "Identify engagement challenges",
            "Analyze workforce concerns",
            "Recommend corrective interventions"
        ],

        "task":
        """
Develop a business-focused prompt using the RCTCF framework.

Ensure your prompt:
- Includes workforce morale considerations
- Requests actionable recommendations
- Uses structured output format
        """
    }

}

# ---------------- SELECT SCENARIO ---------------- #
selected_scenario = st.selectbox(
    "Choose Business Scenario",
    list(scenarios.keys())
)

scenario = scenarios[selected_scenario]

# ---------------- BUSINESS INSIGHT ---------------- #
st.markdown(
    '<div class="section-title">1. Business Insight</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
<div class="section-box">
{scenario['insight']}
</div>
""",
    unsafe_allow_html=True
)

# ---------------- RAW DATA ---------------- #
st.markdown(
    '<div class="section-title">2. Available Raw Data</div>',
    unsafe_allow_html=True
)

for item in scenario["data"]:
    st.markdown(f"• {item}")
# ---------------- OBJECTIVE ---------------- #
st.markdown(
    '<div class="section-title">3. Objective</div>',
    unsafe_allow_html=True
)

for obj in scenario["objective"]:
    st.markdown(f"✅ {obj}")

# ---------------- LEARNER TASK ---------------- #
st.markdown(
    '<div class="section-title">4. Learner Task</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
<div class="section-box">
{scenario['task']}
</div>
""",
    unsafe_allow_html=True
)

# ---------------- PROMPT INPUT ---------------- #
st.markdown(
    '<div class="section-title">5. Create Your Prompt</div>',
    unsafe_allow_html=True
)

user_prompt = st.text_area(
    "Write your structured prompt below",
    height=280,
    placeholder="""
Example:

Role:
Act as an Industrial Safety Consultant.

Context:
...

Task:
...

Constraints:
...

Format:
...
"""
)

# ---------------- PROMPT EVALUATION FUNCTION ---------------- #

def evaluate_prompt(prompt):

    score = 0

    role_score = 0
    context_score = 0
    task_score = 0
    constraint_score = 0
    format_score = 0

    feedback = []

    lower_prompt = prompt.lower()

    # ROLE
    role_keywords = ["act as", "consultant", "expert", "specialist"]

    if any(word in lower_prompt for word in role_keywords):
        role_score = 20
    else:
        feedback.append("Role definition is unclear or missing.")

    # CONTEXT
    if len(prompt) > 150:
        context_score = 20
    elif len(prompt) > 80:
        context_score = 12
        feedback.append("Business context can be more detailed.")
    else:
        feedback.append("Business context is too limited.")

    # TASK
    task_keywords = [
        "analyze",
        "identify",
        "recommend",
        "evaluate",
        "suggest"
    ]

    task_count = sum(
        word in lower_prompt for word in task_keywords
    )

    if task_count >= 3:
        task_score = 20
    elif task_count >= 1:
        task_score = 12
        feedback.append("Task instructions can be more actionable.")
    else:
        feedback.append("Task definition is unclear.")

    # CONSTRAINTS
    constraint_keywords = [
        "practical",
        "cost",
        "limit",
        "minimum",
        "focus"
    ]

    if any(word in lower_prompt for word in constraint_keywords):
        constraint_score = 20
    else:
        feedback.append("Operational constraints are missing.")

    # FORMAT
    format_keywords = [
        "table",
        "format",
        "output",
        "columns",
        "structure"
    ]

    if any(word in lower_prompt for word in format_keywords):
        format_score = 20
    else:
        feedback.append("Output structure is not defined.")

    score = (
        role_score +
        context_score +
        task_score +
        constraint_score +
        format_score
    )

    return {
        "total": score,
        "role": role_score,
        "context": context_score,
        "task": task_score,
        "constraints": constraint_score,
        "format": format_score,
        "feedback": feedback
    }
# ---------------- SUBMIT BUTTON ---------------- #

if st.button("Evaluate Prompt", use_container_width=True):

    if user_prompt.strip() == "":

        st.warning("Please enter your prompt.")

    else:

        result = evaluate_prompt(user_prompt)

        st.markdown(
            '<div class="eval-box">',
            unsafe_allow_html=True
        )

        # ---------------- SCORE DASHBOARD ---------------- #

        st.markdown("## Prompt Quality Assessment")

        score = result["total"]

        score_col1, score_col2 = st.columns([2,1])

        with score_col1:

            st.progress(score / 100)

            st.markdown(f"### Overall Score: {score}/100")

        with score_col2:

            if score >= 80:
                st.success("High Quality Prompt")

            elif score >= 60:
                st.warning("Moderate Quality Prompt")

            else:
                st.error("Needs Improvement")
        # ---------------- COMPONENT BREAKDOWN ---------------- #

        st.markdown("## RCTCF Component Evaluation")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Role", result["role"])

        with col2:
            st.metric("Context", result["context"])

        with col3:
            st.metric("Task", result["task"])

        with col4:
            st.metric("Constraints", result["constraints"])

        with col5:
            st.metric("Format", result["format"])

        # ---------------- FEEDBACK ---------------- #
        # ---------------- BUSINESS READINESS ---------------- #

        st.markdown("## Business Prompting Readiness")

        readiness_col1, readiness_col2, readiness_col3 = st.columns(3)

        with readiness_col1:

            if result["context"] >= 20:
                st.success("Business Context")
            else:
                st.error("Business Context")

        with readiness_col2:

            if result["task"] >= 20:
                st.success("Instruction Clarity")
            else:
                st.error("Instruction Clarity")

        with readiness_col3:

            if result["format"] >= 20:
                st.success("Structured Output")
            else:
                st.error("Structured Output")


        # ---------------- EVALUATION FEEDBACK ---------------- #

        st.markdown("## Evaluation Feedback")

        strengths = []
        improvements = []

        # STRENGTHS

        if result["role"] >= 20:
            strengths.append("Clear expert role definition")

        if result["context"] >= 20:
            strengths.append("Strong business context provided")

        if result["task"] >= 20:
            strengths.append("Action-oriented task instructions")

        if result["constraints"] >= 20:
            strengths.append("Practical operational constraints included")

        if result["format"] >= 20:
            strengths.append("Structured output format defined")

        # IMPROVEMENTS

        if result["role"] < 20:
            improvements.append("Define a more specific business expert role")

        if result["context"] < 20:
            improvements.append("Include richer operational/business context")

        if result["task"] < 20:
            improvements.append("Use clearer analytical instructions")

        if result["constraints"] < 20:
            improvements.append("Add implementation or operational constraints")

        if result["format"] < 20:
            improvements.append("Specify structured output format")

        feedback_col1, feedback_col2 = st.columns(2)

        with feedback_col1:

            st.markdown("### Strength Areas")

            if strengths:
                for item in strengths:
                    st.success(item)

            else:
                st.info("No major strengths identified.")

        with feedback_col2:

            st.markdown("### Improvement Areas")

            if improvements:
                for item in improvements:
                    st.warning(item)

            else:
                st.success("No major improvement areas identified.")
        # ---------------- PROMPT CLASSIFICATION ---------------- #

        st.markdown("## Prompt Classification")

        if score >= 90:

            st.success(
                "Enterprise-Ready Prompt Structure"
            )

        elif score >= 75:

            st.info(
                "Business-Ready Prompt Structure"
            )

        elif score >= 60:

            st.warning(
                "Developing Prompt Structure"
            )

        else:

            st.error(
                "Foundational Prompt Structure"
            )
        # ---------------- PERFORMANCE MESSAGE ---------------- #

        st.markdown("## Evaluation Summary")

        if score >= 80:

            st.success(
                "The prompt demonstrates strong business understanding and structured instruction design."
            )

        elif score >= 60:

            st.info(
                "The prompt has a good foundation but requires stronger contextual clarity and instruction structuring."
            )

        else:

            st.error(
                "The prompt requires improvement in structure, clarity, and business direction."
            )

        # ---------------- RCA GAP ANALYSIS ---------------- #

        st.divider()

        st.markdown("## RCA-Based Gap Analysis")

        if score >= 80:

            st.success(
                "Prompt structure is aligned with business analysis requirements."
            )

        else:

            rca_table = []

            if result["role"] < 20:
                rca_table.append([
                    "Weak Role Definition",
                    "Expert role not clearly specified",
                    "Generic analytical output",
                    "Define domain-specific expert role"
                ])

            if result["context"] < 20:
                rca_table.append([
                    "Limited Business Context",
                    "Insufficient operational details",
                    "Shallow analysis generation",
                    "Include business data and operational conditions"
                ])

            if result["task"] < 20:
                rca_table.append([
                    "Unclear Task Instructions",
                    "Analysis expectations not defined",
                    "AI may generate vague recommendations",
                    "Use actionable verbs like analyze, identify, recommend"
                ])

            if result["constraints"] < 20:
                rca_table.append([
                    "Missing Constraints",
                    "Operational limitations not mentioned",
                    "Recommendations may become impractical",
                    "Add cost, workforce, or operational constraints"
                ])

            if result["format"] < 20:
                rca_table.append([
                    "Undefined Output Format",
                    "Structured output not requested",
                    "Response may become unorganized",
                    "Specify table, bullets, or output columns"
                ])

            st.table({
                "Gap": [row[0] for row in rca_table],
                "Root Cause": [row[1] for row in rca_table],
                "Impact": [row[2] for row in rca_table],
                "Improvement": [row[3] for row in rca_table]
            })

        # ---------------- EXPERT PROMPT ---------------- #

        st.divider()

        st.markdown("## Suggested Expert Prompt")

        expert_prompts = {

            "Scenario 1 — Safety Incident Increase in Night Shift":
            """
Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss safety incidents increased by 22% during night shifts in the Raw Materials division over the last 45 days. Available data includes shift timing, fatigue records, overtime hours, supervisor roster, and safety audit findings.

Task:
Analyze possible causes behind the increase in incidents, identify high-risk operational patterns, and recommend preventive actions to improve safety compliance.

Constraints:
Focus on practical shopfloor interventions with low implementation cost and minimum operational disruption.

Format:
Provide output in:
Observation | Root Cause | Risk Impact | Preventive Action | Priority
            """,

            "Scenario 2 — Low Adoption of Digital Tools":
            """
Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance employees are not regularly using digital inspection applications despite completing training programs.

Task:
Identify adoption barriers and recommend strategies to improve digital tool usage and workforce engagement.

Constraints:
Recommendations should suit industrial workforce environments with varying digital literacy levels.

Format:
Provide output in:
Problem | Root Cause | Recommendation | Expected Outcome
            """,

            "Scenario 3 — Decline in Training Engagement":
            """
Role:
Act as a Learning Engagement Specialist.

Context:
Mandatory compliance training completion dropped significantly among contract workforce employees.

Task:
Analyze reasons for declining completion rates and recommend practical engagement interventions.

Constraints:
Recommendations should be multilingual, operationally practical, and workforce-friendly.

Format:
Provide output in:
Issue | Analysis | Suggested Action | Expected Improvement
            """,

            "Scenario 4 — High Downtime in Equipment":
            """
Role:
Act as a Reliability and Maintenance Expert.

Context:
A critical conveyor system experienced repeated downtime during peak operational hours.

Task:
Identify probable causes of equipment downtime and recommend preventive maintenance improvements.

Constraints:
Recommendations should minimize shutdown time and optimize maintenance cost.

Format:
Provide output in:
Observation | Root Cause | Recommendation | Business Impact
            """,

            "Scenario 5 — Employee Engagement Survey Drop":
            """
Role:
Act as an Employee Engagement Consultant.

Context:
Employee engagement scores reduced significantly after shift restructuring.

Task:
Analyze possible reasons for declining engagement and suggest corrective interventions.

Constraints:
Focus on workforce morale, communication, and practical implementation.

Format:
Provide output in:
Issue | Possible Cause | Recommendation | Expected Impact
            """
        }

        st.code(
            expert_prompts[selected_scenario],
            language="text"
        )

        # ---------------- WHY THIS PROMPT IS BETTER ---------------- #

        st.divider()

        st.markdown("## Why This Prompt Is Better")

        st.markdown("""
✅ Defines a clear business role

✅ Includes operational context and available data

✅ Requests actionable analysis

✅ Applies practical implementation constraints

✅ Uses structured output format for usability

✅ Improves response quality and business relevance
        """)

        st.info(
            "Structured prompts create structured business outcomes."
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

# ---------------- FOOTER ---------------- #
st.markdown(
    """
<div class="footer">
Structured prompts create structured business outcomes.
</div>
""",
    unsafe_allow_html=True
)