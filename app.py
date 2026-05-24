import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Learning and Devlopment",
    page_icon="📘",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=DM+Serif+Display&display=swap');

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background: #f0f4fa;
    color: #1a1a2e;
    font-family: 'Inter', sans-serif;
           .block-container {
    padding-top: 1rem !important;
}

            header[data-testid="stHeader"] {
    display: none !important;
}

.block-container {
    padding-top: 1rem !important;
}


/* ===== SIDEBAR STYLE ===== */
section[data-testid="stSidebar"] {
    background: #0B3D91;
}

/* ===== MAIN TITLE ===== */
.main-header {
    background: linear-gradient(135deg, #0B3D91 0%, #1565C0 60%, #1976D2 100%);
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: -40px;
    right: -40px;
    width: 220px;
    height: 220px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
}

.main-header::after {
    content: '';
    position: absolute;
    bottom: -60px;
    right: 80px;
    width: 160px;
    height: 160px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}

.main-title {
    font-family: 'DM Serif Display', serif;
    font-size: 46px;
    font-weight: 400;
    color: #ffffff;
    margin: 0 0 6px 0;
    letter-spacing: -0.5px;
    line-height: 1.15;
}

.main-subtitle {
    font-size: 17px;
    color: rgba(255,255,255,0.80);
    font-weight: 400;
    margin: 0 0 6px 0;
    letter-spacing: 0.2px;
}

.main-caption {
    font-size: 13px;
    color: rgba(255,255,255,0.55);
    font-weight: 400;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin: 0;
}

/* ===== FRAMEWORK STRIP ===== */
.framework-strip {
    background: #ffffff;
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 28px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 12px rgba(11,61,145,0.06);
}

.framework-title {
    font-size: 13px;
    font-weight: 600;
    color: #0B3D91;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.framework-pill {
    background: #f0f5ff;
    border: 1.5px solid #c7d9f8;
    border-radius: 12px;
    padding: 16px 12px;
    text-align: center;
    transition: 0.2s ease;
}

.framework-pill:hover {
    background: #0B3D91;
    border-color: #0B3D91;
    transform: translateY(-2px);
}

.framework-pill:hover .pill-letter {
    color: #ffffff;
}

.framework-pill:hover .pill-word {
    color: rgba(255,255,255,0.85);
}

.framework-pill:hover .pill-desc {
    color: rgba(255,255,255,0.65);
}

.pill-letter {
    font-family: 'DM Serif Display', serif;
    font-size: 28px;
    color: #0B3D91;
    line-height: 1;
    margin-bottom: 4px;
}

.pill-word {
    font-size: 12px;
    font-weight: 600;
    color: #1a3a6b;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.pill-desc {
    font-size: 11px;
    color: #6b7fa3;
    margin-top: 2px;
}

/* ===== SECTION HEADER ===== */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 28px 0 14px 0;
}

.section-badge {
    background: #0B3D91;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    letter-spacing: 0.5px;
}

.section-title {
    font-size: 17px;
    font-weight: 600;
    color: #0B3D91;
    letter-spacing: -0.2px;
}

/* ===== PROBLEM BOX ===== */
.problem-box {
    background: #ffffff;
    border-radius: 14px;
    padding: 24px 28px;
    border: 1px solid #e2e8f2;
    border-left: 4px solid #0B3D91;
    box-shadow: 0 2px 12px rgba(11,61,145,0.05);
    font-size: 15.5px;
    line-height: 1.7;
    color: #2d3a52;
    margin-bottom: 10px;
}

/* ===== TABLE OVERRIDE ===== */
[data-testid="stTable"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 10px rgba(11,61,145,0.05);
}

[data-testid="stTable"] table {
    background: #ffffff;
}

[data-testid="stTable"] thead tr th {
    background: #0B3D91 !important;
    color: #ffffff !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 12px 18px !important;
    letter-spacing: 0.4px;
    border: none !important;
}

[data-testid="stTable"] tbody tr td {
    padding: 11px 18px !important;
    font-size: 13.5px;
    border-bottom: 1px solid #f0f4fa !important;
    color: #2d3a52;
}

[data-testid="stTable"] tbody tr:hover td {
    background: #f7f9ff !important;
}

[data-testid="stTable"] tbody tr:last-child td {
    border-bottom: none !important;
}
            
            [data-testid="stTable"] thead tr th:last-child {
    text-align: right !important;
}
            
            

/* ===== CHECKLIST ITEMS ===== */
.check-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 9px 0;
    font-size: 14.5px;
    color: #2d3a52;
    border-bottom: 1px solid #f0f4fa;
}

.check-item:last-child {
    border-bottom: none;
}

.check-icon {
    width: 20px;
    height: 20px;
    background: #e8f0fe;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0B3D91;
    font-size: 11px;
    flex-shrink: 0;
    margin-top: 1px;
}

.bullet-icon {
    width: 20px;
    height: 20px;
    background: #fff0e6;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #d96a00;
    font-size: 11px;
    flex-shrink: 0;
    margin-top: 1px;
}

.checklist-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 18px 22px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 10px rgba(11,61,145,0.04);
    margin-bottom: 10px;
}

/* ===== LEARNER TASK BOX ===== */
.task-box {
    background: linear-gradient(135deg, #f0f5ff, #e8f0fe);
    border-radius: 14px;
    padding: 22px 26px;
    border: 1.5px dashed #93b4f0;
    font-size: 15px;
    color: #1a3a6b;
    font-weight: 500;
    line-height: 1.6;
    margin-bottom: 10px;
}

/* ===== SELECT BOX ===== */
[data-testid="stSelectbox"] > div > div {
    border-radius: 12px !important;
    border: 1.5px solid #c7d9f8 !important;
    background: #ffffff !important;
    font-size: 14.5px !important;
    padding: 1px 0 !important;
    box-shadow: 0 2px 8px rgba(11,61,145,0.06) !important;
}

[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: #0B3D91 !important;
    box-shadow: 0 0 0 3px rgba(11,61,145,0.12) !important;
}
            
            [data-testid="stSelectbox"] span,
[data-testid="stSelectbox"] div,
[data-testid="stSelectbox"] p,
[data-baseweb="select"] span,
[data-baseweb="select"] div {
    color: #1a1a2e !important;
}

/* ===== TEXT AREA ===== */
textarea {
    border-radius: 14px !important;
    font-size: 14.5px !important;
    border: 1.5px solid #c7d9f8 !important;
   background: #f7f9ff !important;
    font-family: 'Inter', sans-serif !important;
    line-height: 1.7 !important;
    box-shadow: 0 2px 8px rgba(11,61,145,0.04) !important;
    padding: 16px !important;
    color: #1a1a2e !important;
}

textarea:focus {
    border-color: #0B3D91 !important;
    box-shadow: 0 0 0 3px rgba(11,61,145,0.1) !important;
}

            [data-baseweb="textarea"] textarea {
    color: #1a1a2e !important;
    background: #ffffff !important;
}

[data-baseweb="base-input"] {
    background: #ffffff !important;
}
            

/* ===== BUTTON ===== */
.stButton > button {
    background: linear-gradient(135deg, #0B3D91, #1565C0);
    color: white;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
    border: none;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 16px rgba(11,61,145,0.30);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #062a66, #0B3D91);
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(11,61,145,0.38);
}

.stButton > button:active {
    transform: translateY(0px);
}

/* ===== METRICS ===== */
[data-testid="metric-container"] {
    background: #ffffff;
    border-radius: 14px;
    padding: 16px 14px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 10px rgba(11,61,145,0.05);
    text-align: center;
}

[data-testid="stMetricLabel"] {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: #6b7fa3 !important;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

[data-testid="stMetricValue"] {
    font-size: 30px !important;
    font-weight: 700 !important;
    color: #0B3D91 !important;
}

/* ===== PROGRESS BAR ===== */
[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #0B3D91, #1976D2) !important;
    border-radius: 10px !important;
}

[data-testid="stProgress"] > div > div {
    background: #e2e8f2 !important;
    border-radius: 10px !important;
    height: 10px !important;
}

/* ===== SCORE RING ===== */
.score-ring-wrap {
    display: flex;
    align-items: center;
    gap: 28px;
    background: #ffffff;
    border-radius: 16px;
    padding: 24px 28px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 12px rgba(11,61,145,0.06);
    margin-bottom: 18px;
}

.score-label {
    font-size: 13px;
    color: #6b7fa3;
    font-weight: 500;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.score-value {
    font-family: 'DM Serif Display', serif;
    font-size: 52px;
    color: #0B3D91;
    line-height: 1;
}

.score-sub {
    font-size: 14px;
    color: #6b7fa3;
    margin-top: 4px;
}

/* ===== EVAL BOX ===== */
.eval-section {
    background: #ffffff;
    border-radius: 16px;
    padding: 28px 32px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 12px rgba(11,61,145,0.06);
    margin-bottom: 20px;
}

.eval-heading {
    font-size: 15px;
    font-weight: 700;
    color: #0B3D91;
    letter-spacing: 0.3px;
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1.5px solid #e8f0fe;
}

/* ===== CODE BLOCK ===== */
[data-testid="stCode"] {
    border-radius: 14px !important;
    border: 1px solid #c7d9f8 !important;
    background: #f7f9ff !important;
}

/* ===== ALERTS / STATUS ===== */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    font-size: 14px !important;
}

/* ===== DIVIDER ===== */
hr {
    border: none !important;
    border-top: 1.5px solid #e8f0fe !important;
    margin: 28px 0 !important;
}

/* ===== SCENARIO SELECTOR LABEL ===== */
.select-label {
    font-size: 13px;
    font-weight: 600;
    color: #0B3D91;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    color: #9baac0;
    margin-top: 48px;
    padding: 20px 0;
    font-size: 12.5px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    border-top: 1px solid #e2e8f2;
}

            /* ===== DARK MODE FIX ===== */
[data-testid="stTextArea"] textarea {
    color: #1a1a2e !important;
    background: #ffffff !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #6b7fa3 !important;
}

[data-baseweb="select"] * {
    color: #1a1a2e !important;
}

[data-testid="stSelectbox"] * {
    color: #1a1a2e !important;
}

[data-testid="stAlert"] {
    color: #1a1a2e !important;
}

[data-testid="stAlert"] p {
    color: #1a1a2e !important;
}

.stWarning, .stSuccess, .stError, .stInfo {
    color: #1a1a2e !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #1a1a2e !important;
}

.check-item span {
    color: #2d3a52 !important;
}

.problem-box {
    color: #2d3a52 !important;
}

.task-box {
    color: #1a3a6b !important;
}




</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #
st.markdown("""
<div class="main-header">
    <h1 class="main-title">Learning & Development</h1>
<p class="main-subtitle">Business Prompting Simulation Environment</p>
<p class="main-caption" style="margin-top:8px;">Scenario-Based Prompt Engineering Capability Assessment</p>
</div>
""", unsafe_allow_html=True)


# ---------------- FRAMEWORK ---------------- #
st.markdown("""
<div class="framework-strip">
    <div class="framework-title">Enterprise Prompting Framework — RCTCF</div>
    <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;">
        <div class="framework-pill">
            <div class="pill-letter">R</div>
            <div class="pill-word">Role</div>
            <div class="pill-desc">Define expertise</div>
        </div>
        <div class="framework-pill">
            <div class="pill-letter">C</div>
            <div class="pill-word">Context</div>
            <div class="pill-desc">Business situation</div>
        </div>
        <div class="framework-pill">
            <div class="pill-letter">T</div>
            <div class="pill-word">Task</div>
            <div class="pill-desc">Expected analysis</div>
        </div>
        <div class="framework-pill">
            <div class="pill-letter">C</div>
            <div class="pill-word">Constraints</div>
            <div class="pill-desc">Operational limitations</div>
        </div>
        <div class="framework-pill">
            <div class="pill-letter">F</div>
            <div class="pill-word">Format</div>
            <div class="pill-desc">Output structure</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- SCENARIOS ---------------- #

scenarios = {

"Scenario 1 — Safety Incident Increase in Night Shift": {
    "problem": "Near-miss safety incidents increased by 22% during C-shift (night shift) in Raw Materials division over the last 45 days.",
    "data": {
        "Shift Timing": "A/B/C shift records",
        "Incident Count": "17 incidents in 45 days",
        "Overtime Hours": "Avg 32 hrs/month/operator",
        "Fatigue Score": "Scale 1–5",
        "Supervisor Roster": "Shift-wise allocation",
        "Safety Audit": "PPE non-compliance observed"
    },
    "objective": [
        "Root cause analysis",
        "High-risk pattern identification",
        "Preventive recommendations",
        "Priority action plan"
    ],
    "constraints": [
        "Use only provided datasets",
        "Avoid assumptions",
        "Focus on Raw Materials division",
        "Low-cost practical solutions"
    ],
    "learner_task": "Create enterprise AI prompt using RCTCF framework",
    "good_looks": [
        "Clear role definition",
        "Uses given data only",
        "Structured output",
        "Actionable insights"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Utilization": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Structure": 1,
        "Business Alignment": 1
    }
},

"Scenario 2 — Low Adoption of Digital Inspection App": {
    "problem": "Maintenance teams are not regularly using newly launched digital inspection apps despite completing training.",
    "data": {
        "App Login Frequency": "Weekly login records",
        "Usage Reports": "Department-wise usage",
        "Training Attendance": "Completion records",
        "Employee Age Group": "Demographics",
        "Shift Timing": "Shift-wise usage",
        "User Feedback": "Usability concerns"
    },
    "objective": [
        "Adoption barrier analysis",
        "Engagement improvement strategies",
        "Digital adoption roadmap"
    ],
    "constraints": [
        "Use only available datasets",
        "Avoid tech assumptions",
        "Industrial workforce suitability",
        "Practical implementation focus"
    ],
    "learner_task": "Create AI prompt to identify barriers and improve adoption.",
    "good_looks": [
        "Clear problem definition",
        "Uses given data",
        "Actionable recommendations",
        "Practical approach"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Analytical Thinking": 2,
        "Constraints Usage": 2,
        "Output Clarity": 1,
        "Business Relevance": 1
    }
},

"Scenario 3 — Decline in Training Engagement": {
    "problem": "Compliance training completion dropped from 92% to 61% among contract workforce employees.",
    "data": {
        "LMS Reports": "Completion records",
        "Department Data": "Workforce distribution",
        "Language Preference": "Multilingual workforce",
        "Attendance Records": "Training attendance",
        "Shift Schedules": "Workforce shifts",
        "Mobile Usage": "Device accessibility"
    },
    "objective": [
        "Root cause analysis",
        "Engagement improvement",
        "Completion improvement plan"
    ],
    "constraints": [
        "Multilingual support required",
        "Avoid classroom-heavy methods",
        "Practical operations focus"
    ],
    "learner_task": "Convert business problem into structured AI prompt.",
    "good_looks": [
        "Workforce-aware design",
        "Clear constraints",
        "Actionable structure",
        "Operational relevance"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Understanding": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Structure": 1,
        "Business Alignment": 1
    }
},

"Scenario 4 — High Downtime in Conveyor System": {
    "problem": "Repeated downtime in a critical conveyor system during peak operational hours.",
    "data": {
        "Maintenance Logs": "Repair history",
        "Breakdown Frequency": "Weekly incidents",
        "Equipment Age": "12 years",
        "Downtime Duration": "2.5 hrs avg",
        "Spare Parts": "Frequent replacements",
        "Production Impact": "Dispatch delays"
    },
    "objective": [
        "Root cause identification",
        "Preventive maintenance strategy",
        "Downtime reduction"
    ],
    "constraints": [
        "Minimize shutdown time",
        "Avoid high-cost solutions",
        "Ensure operational continuity"
    ],
    "learner_task": "Create structured AI prompt for maintenance analysis.",
    "good_looks": [
        "Maintenance insight",
        "Data-driven reasoning",
        "Operational focus",
        "Clear structure"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 5 — Employee Engagement Score Drop": {
    "problem": "Engagement scores reduced significantly after shift restructuring in one production department.",
    "data": {
        "Engagement Scores": "Survey results",
        "Shift Changes": "Revised roster",
        "Absenteeism": "14% increase",
        "Employee Feedback": "Communication issues",
        "Overtime": "Increased hours",
        "Attrition": "Early exits"
    },
    "objective": [
        "Engagement gap analysis",
        "Risk prediction",
        "Intervention plan"
    ],
    "constraints": [
        "Only affected department",
        "No compensation-heavy solutions",
        "Focus on morale"
    ],
    "learner_task": "Create AI prompt for workforce engagement analysis.",
    "good_looks": [
        "Clear workforce insight",
        "Actionable output",
        "Structured reasoning",
        "Business relevance"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 6 — High Attrition in Shared Services": {
    "problem": "Young employees are leaving Shared Services within 18 months.",
    "data": {
        "Exit Feedback": "Growth concerns",
        "Tenure": "Avg 14 months",
        "Promotion Data": "Low movement",
        "Compensation": "Market benchmark",
        "Engagement Scores": "Declining",
        "Manager Feedback": "Career clarity issues"
    },
    "objective": [
        "Root cause analysis",
        "Retention strategy",
        "Early warning signals"
    ],
    "constraints": [
        "Focus on Gen Z",
        "No unrealistic compensation assumptions",
        "Scalable solutions"
    ],
    "learner_task": "Design HR analytics AI prompt.",
    "good_looks": [
        "Behavioral insight",
        "Retention logic",
        "Structured analysis",
        "Scalable thinking"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 7 — Overtime Leading to Absenteeism": {
    "problem": "Employees with high overtime show increased absenteeism after 3 months.",
    "data": {
        "Overtime Hours": "Monthly trend",
        "Attendance": "Absenteeism records",
        "Departments": "High overtime areas",
        "Fatigue Reports": "Health data",
        "Productivity": "Output variation",
        "Shifts": "Workforce allocation"
    },
    "objective": [
        "Pattern analysis",
        "Workforce optimization",
        "Preventive planning"
    ],
    "constraints": [
        "Maintain productivity",
        "No manpower increase",
        "Focus on wellbeing"
    ],
    "learner_task": "Build workforce analytics AI prompt.",
    "good_looks": [
        "Fatigue awareness",
        "Operational balance",
        "Data-driven insight",
        "Structured output"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 8 — Slow Recruitment Process": {
    "problem": "Hiring cycle increased from 35 to 62 days for maintenance engineers.",
    "data": {
        "Hiring Stages": "Recruitment timeline",
        "Panel Availability": "Scheduling delays",
        "Offer Acceptance": "Drop trends",
        "Vendor TAT": "Agency delays",
        "Dropouts": "Candidate drop analysis",
        "Urgency": "Position criticality"
    },
    "objective": [
        "Bottleneck analysis",
        "Process improvement",
        "Faster hiring"
    ],
    "constraints": [
        "Maintain hiring quality",
        "No cost increase",
        "Process optimization only"
    ],
    "learner_task": "Create recruitment analysis AI prompt.",
    "good_looks": [
        "Clear bottleneck focus",
        "Hiring insight",
        "Actionable output",
        "Structured thinking"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 9 — Poor Knowledge Retention After Training": {
    "problem": "Operators forget safety procedures within 30 days after training.",
    "data": {
        "Assessment Scores": "Post-training results",
        "Refresher Attendance": "Participation",
        "Incident Reports": "Safety issues",
        "Shift Mapping": "Workforce shifts",
        "Observations": "Supervisor reports",
        "Feedback": "Learning feedback"
    },
    "objective": [
        "Retention improvement",
        "Reinforcement strategy",
        "Effectiveness measurement"
    ],
    "constraints": [
        "No long classroom training",
        "Practical reinforcement only",
        "Shopfloor suitability"
    ],
    "learner_task": "Create training effectiveness AI prompt.",
    "good_looks": [
        "Learning reinforcement",
        "Practical design",
        "Actionable insight",
        "Clear structure"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
},

"Scenario 10 — Low Productivity in C-Shift": {
    "problem": "C-shift productivity is 14% lower than A-shift.",
    "data": {
        "Production": "Shift output",
        "Downtime": "Machine breakdowns",
        "Manpower": "Workforce allocation",
        "Attendance": "Shift attendance",
        "Supervisors": "Leadership mapping",
        "Maintenance": "Equipment reliability"
    },
    "objective": [
        "Productivity gap analysis",
        "Root cause identification",
        "Shift improvement"
    ],
    "constraints": [
        "Operational improvements only",
        "No capex increase",
        "Maintain continuity"
    ],
    "learner_task": "Create productivity analysis AI prompt.",
    "good_looks": [
        "Operational insight",
        "Shift analysis",
        "Actionable output",
        "Structured reasoning"
    ],
    "scorecard": {
        "Role Definition": 2,
        "Data Usage": 2,
        "Task Clarity": 2,
        "Constraints Usage": 2,
        "Output Format": 1,
        "Business Relevance": 1
    }
}

}


# ---------------- SELECT SCENARIO ---------------- #
st.markdown('<div class="select-label">Choose Business Scenario</div>', unsafe_allow_html=True)
selected_scenario = st.selectbox(
    "",
    list(scenarios.keys()),
    label_visibility="collapsed"
)

scenario = scenarios[selected_scenario]

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUSINESS INSIGHT ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">01</span>
    <span class="section-title">Business Insight</span>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="problem-box">{scenario["problem"]}</div>', unsafe_allow_html=True)

# ---------------- RAW DATA ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">02</span>
    <span class="section-title">Available Data</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Dataset": list(scenario["data"].keys()),
    "Details": list(scenario["data"].values())
})

# ---------------- OBJECTIVE ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">03</span>
    <span class="section-title">Objective</span>
</div>
""", unsafe_allow_html=True)

items_html = "".join([
    f'<div class="check-item"><div class="check-icon">✓</div><span>{obj}</span></div>'
    for obj in scenario["objective"]
])
st.markdown(f'<div class="checklist-card">{items_html}</div>', unsafe_allow_html=True)

# ---------------- CONSTRAINTS ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">04</span>
    <span class="section-title">Constraints</span>
</div>
""", unsafe_allow_html=True)

items_html = "".join([
    f'<div class="check-item"><div class="bullet-icon">→</div><span>{item}</span></div>'
    for item in scenario["constraints"]
])
st.markdown(f'<div class="checklist-card">{items_html}</div>', unsafe_allow_html=True)

# ---------------- LEARNER TASK ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">05</span>
    <span class="section-title">Enterprise Prompting Task</span>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="task-box">{scenario["learner_task"]}</div>', unsafe_allow_html=True)

# ---------------- WHAT GOOD LOOKS LIKE ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">06</span>
    <span class="section-title">What Good Looks Like</span>
</div>
""", unsafe_allow_html=True)

items_html = "".join([
    f'<div class="check-item"><div class="check-icon">✓</div><span>{item}</span></div>'
    for item in scenario["good_looks"]
])
st.markdown(f'<div class="checklist-card">{items_html}</div>', unsafe_allow_html=True)

# ---------------- EVALUATION SCORECARD ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">07</span>
    <span class="section-title">Evaluation Scorecard</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Criteria": list(scenario["scorecard"].keys()),
    "Marks": list(scenario["scorecard"].values())
})

# ---------------- PROMPT INPUT ---------------- #
st.markdown("""
<div class="section-header">
    <span class="section-badge">08</span>
    <span class="section-title">Create Your Prompt</span>
</div>
""", unsafe_allow_html=True)

user_prompt = st.text_area(
    "Write your structured prompt below",
    height=280,
    placeholder="""Example:

Role:
Act as an Industrial Safety Consultant.

Context:
...

Task:
...

Constraints:
...

Format:
..."""
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

    role_keywords = ["act as", "consultant", "expert", "specialist"]
    if any(word in lower_prompt for word in role_keywords):
        role_score = 20
    else:
        feedback.append("Role definition is unclear or missing.")

    if len(prompt) > 150:
        context_score = 20
    elif len(prompt) > 80:
        context_score = 12
        feedback.append("Business context can be more detailed.")
    else:
        feedback.append("Business context is too limited.")

    task_keywords = ["analyze", "identify", "recommend", "evaluate", "suggest"]
    task_count = sum(word in lower_prompt for word in task_keywords)
    if task_count >= 3:
        task_score = 20
    elif task_count >= 1:
        task_score = 12
        feedback.append("Task instructions can be more actionable.")
    else:
        feedback.append("Task definition is unclear.")

    constraint_keywords = ["practical", "cost", "limit", "minimum", "focus"]
    if any(word in lower_prompt for word in constraint_keywords):
        constraint_score = 20
    else:
        feedback.append("Operational constraints are missing.")

    format_keywords = ["table", "format", "output", "columns", "structure"]
    if any(word in lower_prompt for word in format_keywords):
        format_score = 20
    else:
        feedback.append("Output structure is not defined.")

    score = role_score + context_score + task_score + constraint_score + format_score

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
st.markdown("<br>", unsafe_allow_html=True)

if st.button("⟶  Evaluate Prompt", use_container_width=True):

    if user_prompt.strip() == "":
        st.warning("Please enter your prompt.")

    else:
        result = evaluate_prompt(user_prompt)
        score = result["total"]

        st.divider()

        # ---------------- SCORE DASHBOARD ---------------- #
        st.markdown("""
        <div class="section-header">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Prompt Quality Assessment</span>
        </div>
        """, unsafe_allow_html=True)

        score_col1, score_col2 = st.columns([3, 1])

        with score_col1:
            if score >= 80:
                badge_color = "#1a7a1a"
                badge_bg = "#e6f7e6"
                badge_label = "High Quality Prompt"
            elif score >= 60:
                badge_color = "#7a5a00"
                badge_bg = "#fff8e0"
                badge_label = "Moderate Quality Prompt"
            else:
                badge_color = "#7a1a1a"
                badge_bg = "#fde8e8"
                badge_label = "Needs Improvement"

            st.markdown(f"""
            <div class="score-ring-wrap">
                <div>
                    <div class="score-label">Overall Score</div>
                    <div class="score-value">{score}<span style="font-size:24px;color:#9baac0;">/100</span></div>
                    <div style="margin-top:10px;">
                        <span style="background:{badge_bg};color:{badge_color};font-size:12px;font-weight:600;padding:5px 14px;border-radius:20px;letter-spacing:0.3px;">{badge_label}</span>
                    </div>
                </div>
                <div style="flex:1;">
                    <div style="height:10px;background:#e2e8f2;border-radius:10px;overflow:hidden;">
                        <div style="width:{score}%;height:100%;background:linear-gradient(90deg,#0B3D91,#1976D2);border-radius:10px;transition:width 1s ease;"></div>
                    </div>
                    <div style="display:flex;justify-content:space-between;margin-top:6px;">
                        <span style="font-size:11px;color:#9baac0;">0</span>
                        <span style="font-size:11px;color:#9baac0;">50</span>
                        <span style="font-size:11px;color:#9baac0;">100</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ---------------- COMPONENT BREAKDOWN ---------------- #
        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">RCTCF Component Evaluation</span>
        </div>
        """, unsafe_allow_html=True)

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

        # ---------------- BUSINESS READINESS ---------------- #
        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Business Prompting Readiness</span>
        </div>
        """, unsafe_allow_html=True)

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
        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Evaluation Feedback</span>
        </div>
        """, unsafe_allow_html=True)

        strengths = []
        improvements = []

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
            st.markdown("**Strength Areas**")
            if strengths:
                for item in strengths:
                    st.success(item)
            else:
                st.info("No major strengths identified.")

        with feedback_col2:
            st.markdown("**Improvement Areas**")
            if improvements:
                for item in improvements:
                    st.warning(item)
            else:
                st.success("No major improvement areas identified.")

        # ---------------- PROMPT CLASSIFICATION ---------------- #
        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Prompt Classification</span>
        </div>
        """, unsafe_allow_html=True)

        if score >= 90:
            st.success("Enterprise-Ready Prompt Structure")
        elif score >= 75:
            st.info("Business-Ready Prompt Structure")
        elif score >= 60:
            st.warning("Developing Prompt Structure")
        else:
            st.error("Foundational Prompt Structure")

        # ---------------- PERFORMANCE MESSAGE ---------------- #
        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Evaluation Summary</span>
        </div>
        """, unsafe_allow_html=True)

        if score >= 80:
            st.success("The prompt demonstrates strong business understanding and structured instruction design.")
        elif score >= 60:
            st.info("The prompt has a good foundation but requires stronger contextual clarity and instruction structuring.")
        else:
            st.error("The prompt requires improvement in structure, clarity, and business direction.")

        # ---------------- RCA GAP ANALYSIS ---------------- #
        st.divider()
        st.markdown("""
        <div class="section-header">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">RCA-Based Gap Analysis</span>
        </div>
        """, unsafe_allow_html=True)

        if score >= 80:
            st.success("Prompt structure is aligned with business analysis requirements.")
        else:
            rca_table = []
            if result["role"] < 20:
                rca_table.append(["Weak Role Definition", "Expert role not clearly specified", "Generic analytical output", "Define domain-specific expert role"])
            if result["context"] < 20:
                rca_table.append(["Limited Business Context", "Insufficient operational details", "Shallow analysis generation", "Include business data and operational conditions"])
            if result["task"] < 20:
                rca_table.append(["Unclear Task Instructions", "Analysis expectations not defined", "AI may generate vague recommendations", "Use actionable verbs like analyze, identify, recommend"])
            if result["constraints"] < 20:
                rca_table.append(["Missing Constraints", "Operational limitations not mentioned", "Recommendations may become impractical", "Add cost, workforce, or operational constraints"])
            if result["format"] < 20:
                rca_table.append(["Undefined Output Format", "Structured output not requested", "Response may become unorganized", "Specify table, bullets, or output columns"])

            st.table({
                "Gap": [row[0] for row in rca_table],
                "Root Cause": [row[1] for row in rca_table],
                "Impact": [row[2] for row in rca_table],
                "Improvement": [row[3] for row in rca_table]
            })

        # ---------------- EXPERT PROMPT ---------------- #
        st.divider()
        st.markdown("""
        <div class="section-header">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Suggested Expert Prompt</span>
        </div>
        """, unsafe_allow_html=True)

        expert_prompts = {
            "Scenario 1 — Safety Incident Increase in Night Shift": """Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss safety incidents increased by 22% during night shifts in the Raw Materials division over the last 45 days. Available data includes shift timing, fatigue records, overtime hours, supervisor roster, and safety audit findings.

Task:
Analyze possible causes behind the increase in incidents, identify high-risk operational patterns, and recommend preventive actions to improve safety compliance.

Constraints:
Focus on practical shopfloor interventions with low implementation cost and minimum operational disruption.

Format:
Provide output in:
Observation | Root Cause | Risk Impact | Preventive Action | Priority""",

            "Scenario 2 — Low Adoption of Digital Inspection App": """Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance employees are not regularly using digital inspection applications despite completing training programs.

Task:
Identify adoption barriers and recommend strategies to improve digital tool usage and workforce engagement.

Constraints:
Recommendations should suit industrial workforce environments with varying digital literacy levels.

Format:
Provide output in:
Problem | Root Cause | Recommendation | Expected Outcome""",

            "Scenario 3 — Decline in Training Engagement": """Role:
Act as a Learning Engagement Specialist.

Context:
Mandatory compliance training completion dropped significantly among contract workforce employees.

Task:
Analyze reasons for declining completion rates and recommend practical engagement interventions.

Constraints:
Recommendations should be multilingual, operationally practical, and workforce-friendly.

Format:
Provide output in:
Issue | Analysis | Suggested Action | Expected Improvement""",

            "Scenario 4 — High Downtime in Conveyor System": """Role:
Act as a Reliability and Maintenance Expert.

Context:
A critical conveyor system experienced repeated downtime during peak operational hours.

Task:
Identify probable causes of equipment downtime and recommend preventive maintenance improvements.

Constraints:
Recommendations should minimize shutdown time and optimize maintenance cost.

Format:
Provide output in:
Observation | Root Cause | Recommendation | Business Impact""",

            "Scenario 5 — Employee Engagement Score Drop": """Role:
Act as an Employee Engagement Consultant.

Context:
Employee engagement scores reduced significantly after shift restructuring.

Task:
Analyze possible reasons for declining engagement and suggest corrective interventions.

Constraints:
Focus on workforce morale, communication, and practical implementation.

Format:
Provide output in:
Issue | Possible Cause | Recommendation | Expected Impact""",

            "Scenario 6 — High Attrition in Shared Services": """Role:
Act as an HR Analytics Consultant.

Context:
Young employees are leaving Shared Services within 18 months, citing growth and career clarity concerns.

Task:
Identify root causes of early attrition and recommend scalable retention strategies for Gen Z workforce.

Constraints:
Avoid unrealistic compensation assumptions. Focus on scalable, low-cost interventions.

Format:
Provide output in:
Attrition Driver | Root Cause | Retention Strategy | Expected Impact""",

            "Scenario 7 — Overtime Leading to Absenteeism": """Role:
Act as a Workforce Analytics Specialist.

Context:
Employees with consistently high overtime hours are showing increased absenteeism after 3 months.

Task:
Identify patterns between overtime and absenteeism, and recommend workforce optimization strategies.

Constraints:
Maintain productivity levels. No manpower addition. Focus on wellbeing.

Format:
Provide output in:
Pattern | Root Cause | Recommendation | Expected Outcome""",

            "Scenario 8 — Slow Recruitment Process": """Role:
Act as a Talent Acquisition Process Consultant.

Context:
The hiring cycle for maintenance engineers has increased from 35 to 62 days due to multiple bottlenecks.

Task:
Identify bottlenecks in the recruitment process and recommend improvements to reduce hiring turnaround time.

Constraints:
Maintain hiring quality. No budget increase. Focus on process optimization only.

Format:
Provide output in:
Stage | Bottleneck | Root Cause | Recommendation | Priority""",

            "Scenario 9 — Poor Knowledge Retention After Training": """Role:
Act as a Learning Effectiveness Consultant.

Context:
Operators are forgetting safety procedures within 30 days of completing training.

Task:
Analyze knowledge retention gaps and recommend reinforcement strategies to improve safety recall.

Constraints:
No long classroom-based methods. Shopfloor-suitable and practical reinforcement only.

Format:
Provide output in:
Retention Gap | Root Cause | Reinforcement Strategy | Measurement Indicator""",

            "Scenario 10 — Low Productivity in C-Shift": """Role:
Act as an Operations Productivity Analyst.

Context:
C-shift consistently shows 14% lower productivity compared to A-shift across the same production line.

Task:
Analyze the productivity gap, identify root causes, and recommend operational improvements.

Constraints:
Operational improvements only. No capital expenditure increase. Maintain shift continuity.

Format:
Provide output in:
Productivity Factor | Gap Observed | Root Cause | Recommended Action | Priority"""
        }

        st.code(expert_prompts[selected_scenario], language="text")

        # ---------------- WHY THIS PROMPT IS BETTER ---------------- #
        st.divider()
        st.markdown("""
        <div class="section-header">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Why This Prompt Is Better</span>
        </div>
        """, unsafe_allow_html=True)

        items_html = "".join([
            f'<div class="check-item"><div class="check-icon">✓</div><span>{item}</span></div>'
            for item in [
                "Defines a clear business role",
                "Includes operational context and available data",
                "Requests actionable analysis",
                "Applies practical implementation constraints",
                "Uses structured output format for usability",
                "Improves response quality and business relevance"
            ]
        ])
        st.markdown(f'<div class="checklist-card">{items_html}</div>', unsafe_allow_html=True)

        st.info("Structured prompts create structured business outcomes.")

# ---------------- FOOTER ---------------- #
st.markdown("""
<div class="footer">
    Digital Capability — Data & AI
</div>
""", unsafe_allow_html=True)
