import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import json
import re

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY is missing in .env file")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(
    page_title="Learning and Devlopment",
    page_icon="📘",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=DM+Serif+Display&display=swap');

.stApp {
    background: #f0f4fa;
    color: #1a1a2e;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 1rem !important;
}

header[data-testid="stHeader"] {
    display: none !important;
}

section[data-testid="stSidebar"] {
    background: #0B3D91;
}

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

.framework-pill:hover .pill-letter { color: #ffffff; }
.framework-pill:hover .pill-word { color: rgba(255,255,255,0.85); }
.framework-pill:hover .pill-desc { color: rgba(255,255,255,0.65); }

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

.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 20px 0 10px 0;
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

.problem-box {
    background: #ffffff;
    border-radius: 14px;
    padding: 18px 22px;
    border: 1px solid #e2e8f2;
    border-left: 4px solid #0B3D91;
    box-shadow: 0 2px 12px rgba(11,61,145,0.05);
    font-size: 14.5px;
    line-height: 1.7;
    color: #2d3a52;
    margin-bottom: 10px;
}

[data-testid="stTable"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 10px rgba(11,61,145,0.05);
}

[data-testid="stTable"] table { background: #ffffff; }

[data-testid="stTable"] thead tr th {
    background: #0B3D91 !important;
    color: #ffffff !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 10px 14px !important;
    letter-spacing: 0.4px;
    border: none !important;
}

[data-testid="stTable"] tbody tr td {
    padding: 9px 14px !important;
    font-size: 13px;
    border-bottom: 1px solid #f0f4fa !important;
    color: #2d3a52;
}

[data-testid="stTable"] tbody tr:hover td { background: #f7f9ff !important; }
[data-testid="stTable"] tbody tr:last-child td { border-bottom: none !important; }
[data-testid="stTable"] thead tr th:last-child { text-align: right !important; }

.check-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 7px 0;
    font-size: 13.5px;
    color: #2d3a52;
    border-bottom: 1px solid #f0f4fa;
}

.check-item:last-child { border-bottom: none; }

.check-icon {
    width: 18px;
    height: 18px;
    background: #e8f0fe;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0B3D91;
    font-size: 10px;
    flex-shrink: 0;
    margin-top: 1px;
}

.bullet-icon {
    width: 18px;
    height: 18px;
    background: #fff0e6;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #d96a00;
    font-size: 10px;
    flex-shrink: 0;
    margin-top: 1px;
}

.checklist-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 14px 18px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 10px rgba(11,61,145,0.04);
    margin-bottom: 10px;
}

.task-box {
    background: linear-gradient(135deg, #f0f5ff, #e8f0fe);
    border-radius: 14px;
    padding: 16px 20px;
    border: 1.5px dashed #93b4f0;
    font-size: 14px;
    color: #1a3a6b;
    font-weight: 500;
    line-height: 1.6;
    margin-bottom: 10px;
}

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

textarea {
    border-radius: 14px !important;
    font-size: 14px !important;
    border: 1.5px solid #c7d9f8 !important;
    background: #f7f9ff !important;
    font-family: 'Inter', sans-serif !important;
    line-height: 1.7 !important;
    box-shadow: 0 2px 8px rgba(11,61,145,0.04) !important;
    padding: 14px !important;
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

[data-baseweb="base-input"] { background: #ffffff !important; }

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

.stButton > button:active { transform: translateY(0px); }

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

[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #0B3D91, #1976D2) !important;
    border-radius: 10px !important;
}

[data-testid="stProgress"] > div > div {
    background: #e2e8f2 !important;
    border-radius: 10px !important;
    height: 10px !important;
}

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

[data-testid="stCode"] {
    border-radius: 14px !important;
    border: 1px solid #c7d9f8 !important;
    background: #f7f9ff !important;
}

[data-testid="stAlert"] {
    border-radius: 12px !important;
    font-size: 14px !important;
}
            
/* FIX EXPANDER BLACK HOVER ISSUE */

details {
    background: transparent !important;
}

details summary {
    background: #f4f7fc !important;
    color: #1a1a2e !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    border: 1px solid #dbe6f7 !important;
    font-weight: 600 !important;
}

details summary:hover {
    background: #eef3fb !important;
    color: #0B3D91 !important;
}

details[open] summary {
    background: #eef3fb !important;
    color: #0B3D91 !important;
}

summary {
    list-style: none !important;
}

summary::-webkit-details-marker {
    display: none;
}




hr {
    border: none !important;
    border-top: 1.5px solid #e8f0fe !important;
    margin: 20px 0 !important;
}

.select-label {
    font-size: 13px;
    font-weight: 600;
    color: #0B3D91;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

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

.left-panel {
    background: #ffffff;
    border-radius: 16px;
    padding: 20px 24px;
    border: 1px solid #e2e8f2;
    box-shadow: 0 2px 12px rgba(11,61,145,0.06);
    height: fit-content;
}

.right-panel {
    background: transparent;
    border-radius: 16px;
    padding: 0px;
    border: none;
    box-shadow: none;
}

[data-testid="stTextArea"] textarea {
    color: #1a1a2e !important;
    background: #ffffff !important;
}

[data-testid="stTextArea"] textarea::placeholder { color: #6b7fa3 !important; }
[data-baseweb="select"] * { color: #1a1a2e !important; }
[data-testid="stSelectbox"] * { color: #1a1a2e !important; }
[data-testid="stAlert"] { color: #1a1a2e !important; }
[data-testid="stAlert"] p { color: #1a1a2e !important; }
.stWarning, .stSuccess, .stError, .stInfo { color: #1a1a2e !important; }
[data-testid="stMarkdownContainer"] p { color: #1a1a2e !important; }
.check-item span { color: #2d3a52 !important; }
.problem-box { color: #2d3a52 !important; }
.task-box { color: #1a3a6b !important; }

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
    
    
    "good_looks": [
        "Clear role definition",
        "Uses given data only",
        "Structured output",
        "Actionable insights"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Utilization": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Structure": 10,
        "Business Alignment": 10
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
     
    
    "good_looks": [
        "Clear problem definition",
        "Uses given data",
        "Actionable recommendations",
        "Practical approach"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Analytical Thinking": 20,
        "Constraints Usage": 20,
        "Output Clarity": 10,
        "Business Relevance": 10
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
    "good_looks": [
        "Workforce-aware design",
        "Clear constraints",
        "Actionable structure",
        "Operational relevance"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Understanding": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Structure": 10,
        "Business Alignment": 10
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
    
    "good_looks": [
        "Maintenance insight",
        "Data-driven reasoning",
        "Operational focus",
        "Clear structure"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
    
    "good_looks": [
        "Clear workforce insight",
        "Actionable output",
        "Structured reasoning",
        "Business relevance"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
    
    "good_looks": [
        "Behavioral insight",
        "Retention logic",
        "Structured analysis",
        "Scalable thinking"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
    
    "good_looks": [
        "Fatigue awareness",
        "Operational balance",
        "Data-driven insight",
        "Structured output"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
    
    "good_looks": [
        "Clear bottleneck focus",
        "Hiring insight",
        "Actionable output",
        "Structured thinking"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
    
    "good_looks": [
        "Learning reinforcement",
        "Practical design",
        "Actionable insight",
        "Clear structure"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
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
     
    
    "good_looks": [
        "Operational insight",
        "Shift analysis",
        "Actionable output",
        "Structured reasoning"
    ],
    "scorecard": {
        "Role Definition": 20,
        "Data Usage": 20,
        "Task Clarity": 20,
        "Constraints Usage": 20,
        "Output Format": 10,
        "Business Relevance": 10
    }
}

}

expert_prompts = {
    "Scenario 1 — Safety Incident Increase in Night Shift": """Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss safety incidents increased by 22% during night shifts in the Raw Materials division over the last 45 days. Available data includes shift timing, fatigue records, overtime hours, supervisor roster, and safety audit findings.

Task:
Analyze possible causes behind the increase in incidents, identify high-risk operational patterns, and recommend preventive actions to improve safety compliance.

Format:
Provide output in:
Observation | Root Cause | Risk Impact | Preventive Action | Priority""",

    "Scenario 2 — Low Adoption of Digital Inspection App": """Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance employees are not regularly using digital inspection applications despite completing training programs.

Task:
Identify adoption barriers and recommend strategies to improve digital tool usage and workforce engagement.

Format:
Provide output in:
Problem | Root Cause | Recommendation | Expected Outcome""",

    "Scenario 3 — Decline in Training Engagement": """Role:
Act as a Learning Engagement Specialist.

Context:
Mandatory compliance training completion dropped significantly among contract workforce employees.

Task:
Analyze reasons for declining completion rates and recommend practical engagement interventions.


Format:
Provide output in:
Issue | Analysis | Suggested Action | Expected Improvement""",

    "Scenario 4 — High Downtime in Conveyor System": """Role:
Act as a Reliability and Maintenance Expert.

Context:
A critical conveyor system experienced repeated downtime during peak operational hours.

Task:
Identify probable causes of equipment downtime and recommend preventive maintenance improvements.


Format:
Provide output in:
Observation | Root Cause | Recommendation | Business Impact""",

    "Scenario 5 — Employee Engagement Score Drop": """Role:
Act as an Employee Engagement Consultant.

Context:
Employee engagement scores reduced significantly after shift restructuring.

Task:
Analyze possible reasons for declining engagement and suggest corrective interventions.


Format:
Provide output in:
Issue | Possible Cause | Recommendation | Expected Impact""",

    "Scenario 6 — High Attrition in Shared Services": """Role:
Act as an HR Analytics Consultant.

Context:
Young employees are leaving Shared Services within 18 months, citing growth and career clarity concerns.

Task:
Identify root causes of early attrition and recommend scalable retention strategies for Gen Z workforce.

Format:
Provide output in:
Attrition Driver | Root Cause | Retention Strategy | Expected Impact""",

    "Scenario 7 — Overtime Leading to Absenteeism": """Role:
Act as a Workforce Analytics Specialist.

Context:
Employees with consistently high overtime hours are showing increased absenteeism after 3 months.

Task:
Identify patterns between overtime and absenteeism, and recommend workforce optimization strategies.


Format:
Provide output in:
Pattern | Root Cause | Recommendation | Expected Outcome""",

    "Scenario 8 — Slow Recruitment Process": """Role:
Act as a Talent Acquisition Process Consultant.

Context:
The hiring cycle for maintenance engineers has increased from 35 to 62 days due to multiple bottlenecks.

Task:
Identify bottlenecks in the recruitment process and recommend improvements to reduce hiring turnaround time.



Format:
Provide output in:
Stage | Bottleneck | Root Cause | Recommendation | Priority""",

    "Scenario 9 — Poor Knowledge Retention After Training": """Role:
Act as a Learning Effectiveness Consultant.

Context:
Operators are forgetting safety procedures within 30 days of completing training.

Task:
Analyze knowledge retention gaps and recommend reinforcement strategies to improve safety recall.

Format:
Provide output in:
Retention Gap | Root Cause | Reinforcement Strategy | Measurement Indicator""",

    "Scenario 10 — Low Productivity in C-Shift": """Role:
Act as an Operations Productivity Analyst.

Context:
C-shift consistently shows 14% lower productivity compared to A-shift across the same production line.

Task:
Analyze the productivity gap, identify root causes, and recommend operational improvements.


Format:
Provide output in:
Productivity Factor | Gap Observed | Root Cause | Recommended Action | Priority"""
}


# ---------------- SCENARIO SELECTOR ---------------- #
st.markdown('<div class="select-label">Choose Business Scenario</div>', unsafe_allow_html=True)
selected_scenario = st.selectbox(
    "",
    list(scenarios.keys()),
    label_visibility="collapsed"
)

scenario = scenarios[selected_scenario]

st.markdown("<br>", unsafe_allow_html=True)



# ---------------- BUSINESS SUMMARY ---------------- #

st.markdown("""
<div class="section-header">
    <span class="section-badge">Scenario Overview</span>
    <span class="section-title">Business Problem & Evaluation Criteria</span>
</div>
""", unsafe_allow_html=True)
top_col1, top_col2 = st.columns([2,1])

with top_col1:

    st.markdown(f"""
    <div class="problem-box" style="padding:16px 20px; line-height:1.5;">

    <b>Business Problem</b><br>
    {scenario["problem"]}

    <br>

    <b>Available Data</b><br>
    • {"<br>• ".join(scenario["data"].keys())}

    <br>

    <b>Objectives</b><br>
    • {"<br>• ".join(scenario["objective"])}

    </div>
    """, unsafe_allow_html=True)
with top_col2:

    st.markdown("""
    <div class="section-header" style="margin-top:0;">
        <span class="section-badge">Evaluation</span>
    </div>
    """, unsafe_allow_html=True)

    st.table({
        "Criteria": list(scenario["scorecard"].keys()),
        "Marks": list(scenario["scorecard"].values())
    })


# ---------------- PROMPT INPUT PANEL ---------------- #

st.markdown('<div class="right-panel">', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <span class="section-badge">02</span>
    <span class="section-title">Create Your Prompt</span>
</div>
""", unsafe_allow_html=True)

user_prompt = st.text_area(
    "Write your structured prompt below",
    height=360,
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

st.markdown("<br>", unsafe_allow_html=True)

evaluate_clicked = st.button("⟶  Evaluate Prompt", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------- GROQ AI EVALUATION FUNCTION --------- #

def evaluate_with_genai(prompt, scenario_name, scenario):

    system_prompt = """
You are a strict prompt quality evaluator for enterprise business scenarios.
Score the user's prompt harshly and accurately using these 4 components (25 marks each, total 100):

ROLE (0-25): Did they define a specific business/domain expert role? 
- 20-25: Clear expert role (e.g. "Act as a Safety Consultant")
- 10-19: Vague role mentioned
- 0-9: No role defined at all

CONTEXT (0-25): Did they include the business situation, data references, or operational details?
- 20-25: Rich context with data points and scenario details
- 10-19: Partial context, missing key details
- 0-9: No meaningful context provided

TASK (0-25): Did they give clear analytical instructions using action verbs (analyze, identify, recommend)?
- 20-25: Clear multi-part task with specific analytical goals
- 10-19: Vague or single-line task
- 0-9: No clear task defined

FORMAT (0-25): Did they specify a structured output format (table columns, bullets, headers)?
- 20-25: Explicit output structure defined
- 10-19: Partially mentioned
- 0-9: No format specified

SCORING RULES:
- A one-liner or casual prompt should score between 25-35 total.
- A missing component scores between 0-5 only, not 10+.
- A vague or implied component scores 5-10, not 15+.
- Score 80+ requires ALL 4 components written clearly and in detail.
- Score 60-79 means 3 components present but at least one is weak.
- Score 40-59 means 2 components present with some detail.
- Score below 40 means only 1 or no components present.
- DO NOT reward implied or assumed components generously.
Total = role + context + task + format. Must add up exactly.

Return ONLY valid JSON with no markdown, no backticks, no explanation:
{
  "total": number,
  "role": number,
  "context": number,
  "task": number,
  "format": number,
  "feedback": ["short feedback points"]
}
"""
    user_message = f"""
Scenario: {scenario_name}

Scenario Data:
{scenario}

User Prompt:
{prompt}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0
    )

    return response.choices[0].message.content
# ------- EVALUATION RESULTS BELOW BOTH COLUMNS ------- #

if evaluate_clicked:

    if user_prompt.strip() == "":
        st.warning("Please enter your prompt.")

    else:
        with st.spinner("Evaluating your prompt with Groq AI..."):

            raw_result = evaluate_with_genai(
                user_prompt,
                selected_scenario,
                scenario
            )

        try:
            cleaned = raw_result.strip()
            cleaned = re.sub(r"```(?:json)?", "", cleaned)
            cleaned = re.sub(r"```", "", cleaned)
            cleaned = cleaned.strip()

            result = json.loads(cleaned)

        except Exception as e:
            st.error("AI returned invalid JSON. Showing raw output.")
            st.code(raw_result)
            st.stop()

        score = result["total"]

        st.divider()

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

            html_score = f'<div class="score-ring-wrap"><div><div class="score-label">Overall Score</div><div class="score-value">{score}<span style="font-size:24px;color:#9baac0;">/100</span></div><div style="margin-top:10px;"><span style="background:{badge_bg};color:{badge_color};font-size:12px;font-weight:600;padding:5px 14px;border-radius:20px;">{badge_label}</span></div></div><div style="flex:1;"><div style="height:10px;background:#e2e8f2;border-radius:10px;overflow:hidden;"><div style="width:{score}%;height:100%;background:linear-gradient(90deg,#0B3D91,#1976D2);border-radius:10px;"></div></div></div></div>'
            st.markdown(html_score, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-header" style="margin-top:24px;">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">RCTF Component Evaluation</span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Role", result["role"])

        with col2:
            st.metric("Context", result["context"])

        with col3:
            st.metric("Task", result["task"])

        with col4:
            st.metric("Format", result["format"])

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

        if result["format"] >= 20:
            strengths.append("Structured output format defined")

        if result["role"] < 20:
            improvements.append("Define a more specific business expert role")

        if result["context"] < 20:
            improvements.append("Include richer operational/business context")

        if result["task"] < 20:
            improvements.append("Use clearer analytical instructions")

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

            if result["format"] < 20:
                rca_table.append([
                    "Undefined Output Format",
                    "Structured output not requested",
                    "Response may become unorganized",
                    "Specify table, bullets, or output columns"
                ])

            if rca_table:

                st.table({
                    "Gap": [row[0] for row in rca_table],
                    "Root Cause": [row[1] for row in rca_table],
                    "Impact": [row[2] for row in rca_table],
                    "Improvement": [row[3] for row in rca_table]
                })

        st.divider()

        st.markdown("""
        <div class="section-header">
            <span class="section-badge" style="background:#1565C0;">◈</span>
            <span class="section-title">Suggested Expert Prompt</span>
        </div>
        """, unsafe_allow_html=True)

        st.code(expert_prompts[selected_scenario], language="text")

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
                "Uses structured output format for usability",
                "Improves response quality and business relevance"
            ]
        ])

        st.markdown(
            f'<div class="checklist-card">{items_html}</div>',
            unsafe_allow_html=True
        )

        st.info("Structured prompts improve business clarity, analytical thinking, and AI response quality.")


        #----FOOTER-------#
st.markdown("""
<div class="footer">
    Digital Capability — Data & AI
</div>
""", unsafe_allow_html=True)