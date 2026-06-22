import streamlit as st
import json, os
from datetime import date, datetime

st.set_page_config(page_title="Data Engineer Portfolio", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

DATA_FILE = "portfolio_data.json"
DEFAULT_DATA = {
    "profile": {
        "name": "Your Name",
        "title": "Data Engineer | Fresher",
        "tagline": "Building reliable data pipelines that turn raw data into business value.",
        "email": "youremail@gmail.com",
        "phone": "+91 XXXXXXXXXX",
        "location": "Mumbai, India",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourusername",
        "resume_link": "https://drive.google.com/your-resume-link",
        "leetcode": "https://leetcode.com/yourusername",
        "kaggle": "https://kaggle.com/yourusername",
        "medium": "",
        "about": "I am a passionate Data Engineer fresher with hands-on experience building ETL pipelines, working with cloud platforms, and transforming raw data into actionable insights."
    },
    "skills": {
        "Languages": ["Python", "SQL", "DSA / OOPs"],
        "Big Data & ETL": ["ETL Pipelines", "Apache Airflow", "dbt", "Window Functions", "CTEs", "SCD (Slowly Changing Dimensions)"],
        "Cloud Platforms": ["AWS", "Azure (Basics)", "Snowflake"],
        "Databases": ["PostgreSQL", "MySQL", "MongoDB"],
        "Tools & DevOps": ["Git / GitHub", "Docker", "Linux"],
        "Visualization": ["Power BI", "Tableau"]
    },
    "experience": [
        {
            "id": 1,
            "role": "Data Engineering Intern",
            "company": "Company Name",
            "duration": "Jun 2024 – Aug 2024",
            "location": "Mumbai / Remote",
            "points": [
                "Built an ETL pipeline using Python and Apache Airflow that reduced data processing time by 40%.",
                "Designed and optimized SQL queries for a PostgreSQL data warehouse serving 5+ business teams.",
                "Automated daily reporting workflows using AWS Lambda and S3, saving 3 hours of manual work per day."
            ]
        }
    ],
    "education": [
        {
            "id": 1,
            "degree": "B.E. / B.Tech in Computer Engineering",
            "institution": "Your University Name",
            "year": "2020 – 2024",
            "score": "CGPA: 8.2 / 10",
            "highlights": ["Relevant coursework: DBMS, Data Structures, Cloud Computing, Big Data Analytics"]
        }
    ],
    "certifications": [
        {"id": 1, "name": "AWS Certified Cloud Practitioner", "issuer": "Amazon Web Services", "year": "2024", "link": ""},
        {"id": 2, "name": "Google Professional Data Engineer", "issuer": "Google Cloud", "year": "2024", "link": ""},
        {"id": 3, "name": "dbt Fundamentals", "issuer": "dbt Labs", "year": "2024", "link": ""}
    ],
    "projects": [
        {
            "id": 1,
            "title": "Real-Time Streaming Pipeline",
            "description": "End-to-end real-time data pipeline using Kafka, Spark Streaming, and Cassandra for processing 1M+ events/day.",
            "tech": ["Python", "Apache Kafka", "Apache Spark", "Cassandra", "Docker"],
            "github": "https://github.com/yourusername/streaming-pipeline",
            "demo": "",
            "status": "Completed",
            "progress": 100,
            "tasks": [
                {"task": "Kafka producer & consumer setup", "done": True},
                {"task": "Spark Streaming integration", "done": True},
                {"task": "Docker Compose orchestration", "done": True}
            ],
            "highlight": True,
            "category": "Streaming",
            "started": "2024-01-15",
            "completed": "2024-02-28"
        }
    ],
    "achievements": [
        "Ranked in top 10% on Kaggle Tabular Playground Series competitions.",
        "Solved 200+ DSA problems on LeetCode (Rating: 1500+).",
        "Open-source contributor to Apache Airflow providers.",
        "Best Project Award at college tech fest for capstone project."
    ]
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    save_data(DEFAULT_DATA)
    return DEFAULT_DATA

def save_data(d):
    with open(DATA_FILE, "w") as f:
        json.dump(d, f, indent=2)

data = load_data()

# ── Mode ──────────────────────────────────────────────────────────────────────
qp = st.query_params
# Default is visitor (public site) — owner mode only via ?mode=owner
VISITOR = qp.get("mode", "visitor") != "owner"

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}

/* hero */
.hero{background:linear-gradient(135deg,#0d1117,#161b22);border:1px solid #21262d;border-radius:16px;padding:40px 36px;margin-bottom:28px;position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;top:-50%;right:-10%;width:400px;height:400px;background:radial-gradient(circle,rgba(88,166,255,0.08) 0%,transparent 70%);pointer-events:none;}
.hero-name{font-size:2.6rem;font-weight:800;color:#e6edf3;margin:0;letter-spacing:-0.5px;}
.hero-title{font-family:'JetBrains Mono',monospace;font-size:1rem;color:#58a6ff;margin:8px 0 14px;}
.hero-tagline{font-size:1rem;color:#8b949e;max-width:600px;line-height:1.75;}

/* cards */
.card{background:#161b22;border:1px solid #21262d;border-radius:12px;padding:22px;margin-bottom:14px;}
.card-hl{border-left:3px solid #58a6ff;}

/* section headers */
.sh{font-size:1.3rem;font-weight:700;color:#e6edf3;margin:28px 0 16px;display:flex;align-items:center;gap:10px;}
.sh::after{content:'';flex:1;height:1px;background:#21262d;margin-left:12px;}

/* badges */
.badge{display:inline-block;background:rgba(88,166,255,0.1);color:#58a6ff;border:1px solid rgba(88,166,255,0.3);border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:600;margin:3px 3px 3px 0;}
.badge-g{background:rgba(63,185,80,0.1);color:#3fb950;border-color:rgba(63,185,80,0.3);}
.badge-o{background:rgba(210,153,34,0.1);color:#d2a22a;border-color:rgba(210,153,34,0.3);}
.badge-p{background:rgba(188,140,255,0.1);color:#bc8cff;border-color:rgba(188,140,255,0.3);}
.badge-r{background:rgba(248,81,73,0.1);color:#f85149;border-color:rgba(248,81,73,0.3);}

/* skill pills */
.sp{display:inline-block;background:#21262d;color:#c9d1d9;border-radius:6px;padding:4px 12px;font-size:0.82rem;font-family:'JetBrains Mono',monospace;margin:3px;border:1px solid #30363d;}
.sp-proved{background:rgba(88,166,255,0.12);color:#58a6ff;border-color:rgba(88,166,255,0.4);font-weight:600;}

/* progress */
.pw{background:#21262d;border-radius:4px;height:8px;overflow:hidden;margin:8px 0;}
.pf{height:100%;border-radius:4px;background:linear-gradient(90deg,#238636,#3fb950);}
.pf-mid{background:linear-gradient(90deg,#9e6a03,#d2a22a);}
.pf-low{background:linear-gradient(90deg,#6e40c9,#bc8cff);}

/* link buttons */
.lb{display:inline-block;background:#21262d;color:#58a6ff!important;border:1px solid #30363d;border-radius:8px;padding:7px 16px;font-size:0.84rem;font-weight:600;text-decoration:none!important;margin:3px 3px 0 0;transition:all 0.2s;}
.lb:hover{background:#30363d;border-color:#58a6ff;}
.lb-p{background:#238636;color:#fff!important;border-color:#2ea043;}
.lb-p:hover{background:#2ea043;}

/* timeline */
.tl{border-left:2px solid #21262d;padding-left:20px;margin-bottom:22px;position:relative;}
.tl::before{content:'';position:absolute;left:-6px;top:6px;width:10px;height:10px;border-radius:50%;background:#58a6ff;border:2px solid #0d1117;}

/* stat box */
.sb{background:#161b22;border:1px solid #21262d;border-radius:10px;padding:18px;text-align:center;}
.sn{font-size:1.9rem;font-weight:800;color:#58a6ff;font-family:'JetBrains Mono',monospace;}
.sl{font-size:0.8rem;color:#8b949e;margin-top:4px;}

/* resume banner */
.rb{background:linear-gradient(135deg,#1f2937,#111827);border:1px solid #374151;border-left:4px solid #58a6ff;border-radius:10px;padding:18px 22px;margin-bottom:18px;}

/* hire banner */
.hb{background:linear-gradient(135deg,rgba(35,134,54,0.15),rgba(88,166,255,0.1));border:1px solid rgba(63,185,80,0.4);border-radius:12px;padding:18px 22px;margin-bottom:22px;}

/* footer */
.ft{text-align:center;color:#8b949e;font-size:0.8rem;padding:28px 0 12px;border-top:1px solid #21262d;margin-top:40px;}

/* mobile responsive */
@media(max-width:768px){
  .hero-name{font-size:1.8rem!important;}
  .hero{padding:22px 16px!important;}
  .card{padding:14px!important;}
  .sh{font-size:1.1rem!important;}
}

/* streamlit button overrides */
.stButton>button{background:#238636;color:white;border:none;border-radius:8px;font-weight:600;}
.stButton>button:hover{background:#2ea043;}
div[data-testid="stSidebar"]{background:#0d1117;border-right:1px solid #21262d;}
div[data-testid="stExpander"]{background:#161b22;border:1px solid #21262d;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def pbar(pct):
    cls = "pf" if pct >= 80 else ("pf pf-mid" if pct >= 40 else "pf pf-low")
    return f'<div class="pw"><div class="{cls}" style="width:{pct}%"></div></div>'

STATUS_BADGE = {"Completed":"badge-g","In Progress":"badge-o","Planning":"badge-p","On Hold":"badge-r"}
STATUS_COLOR = {"Completed":"#3fb950","In Progress":"#d2a22a","Planning":"#bc8cff","On Hold":"#f85149"}

def sbadge(status):
    return f'<span class="badge {STATUS_BADGE.get(status, "")}">{status}</span>'

def get_projects_for_skill(skill):
    matches = []
    sk = skill.lower().strip()
    for pr in data["projects"]:
        for t in pr.get("tech", []):
            if sk in t.lower() or t.lower() in sk:
                matches.append(pr)
                break
    return matches

def next_id(lst):
    return max((x.get("id", 0) for x in lst), default=0) + 1

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    p = data["profile"]
    name = p.get("name", "")
    words = [w for w in name.split() if w]
    initials = (words[0][0] + (words[1][0] if len(words) > 1 else "")).upper() if words else "DE"

    st.markdown(f"""
    <div style="text-align:center;padding:16px 0 8px;">
        <div style="width:76px;height:76px;border-radius:50%;
                    background:linear-gradient(135deg,#58a6ff,#bc8cff);
                    margin:0 auto 12px;display:flex;align-items:center;justify-content:center;
                    font-size:1.7rem;font-weight:800;color:Deep Slate;">{initials}</div>
        <div style="font-weight:800;font-size:1.4rem;color:#1e293b;letter-spacing:-0.2px;">{name}</div>
        <div style="font-size:0.9rem;color:#2563eb;font-family:'JetBrains Mono',monospace;margin-top:6px;">{p['title']}</div>
        <div style="font-size:0.8rem;color:#64748b;margin-top:6px;">📍 {p['location']}</div>
    </div>""", unsafe_allow_html=True)

    if not VISITOR:
        st.markdown('<div style="text-align:center;background:rgba(210,153,34,0.1);border:1px solid rgba(210,153,34,0.3);border-radius:6px;padding:5px 8px;font-size:0.74rem;color:#d2a22a;margin:6px 0;">✏️ Owner Mode &nbsp;·&nbsp; <a href="?mode=visitor" style="color:#d2a22a;text-decoration:underline;">Preview ↗</a></div>', unsafe_allow_html=True)

    st.markdown("---")

    pages_public = {
        "🏠 Home": "home", "👤 About": "about", "💼 Experience": "experience",
        "🚀 Projects": "projects", "🛠 Skills and Certificates": "skills",
        "🎓 Education": "education", "🏆 Achievements": "achievements", "📄 Resume": "resume",
    }
    pages_owner = {"🔗 Share": "links", "⚙️ Edit Profile": "edit"}

    if "page" not in st.session_state:
        st.session_state.page = "home"
    if VISITOR and st.session_state.page in ["links", "edit"]:
        st.session_state.page = "home"

    all_pages = pages_public if VISITOR else {**pages_public, **pages_owner}
    for label, key in all_pages.items():
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key

    st.markdown("---")
    if p.get("linkedin"):    st.markdown(f'<a href="{p["linkedin"]}" target="_blank" class="lb" style="display:block;text-align:center;margin-bottom:5px;">💼 LinkedIn</a>', unsafe_allow_html=True)
    if p.get("github"):      st.markdown(f'<a href="{p["github"]}" target="_blank" class="lb" style="display:block;text-align:center;margin-bottom:5px;">🐙 GitHub</a>', unsafe_allow_html=True)
    if p.get("resume_link"): st.markdown(f'<a href="{p["resume_link"]}" target="_blank" class="lb lb-p" style="display:block;text-align:center;margin-bottom:5px;">📄 Resume</a>', unsafe_allow_html=True)
    if VISITOR and p.get("email"): st.markdown(f'<a href="mailto:{p["email"]}" class="lb lb-p" style="display:block;text-align:center;margin-bottom:5px;">✉ Hire Me</a>', unsafe_allow_html=True)

# ── Page variable ─────────────────────────────────────────────────────────────
page = st.session_state.page
p = data["profile"]

# ════════════════════════════════════════════════════════════
# HOME
# ════════════════════════════════════════════════════════════
if page == "home":
    resume_btn = f'<a href="{p["resume_link"]}" target="_blank" class="lb lb-p">📄 Download Resume</a>' if p.get("resume_link") else ""
    linkedin_btn = f'<a href="{p["linkedin"]}" target="_blank" class="lb">💼 LinkedIn</a>' if p.get("linkedin") else ""
    github_btn = f'<a href="{p["github"]}" target="_blank" class="lb">🐙 GitHub</a>' if p.get("github") else ""
    email_btn = f'<a href="mailto:{p["email"]}" class="lb">✉ Email Me</a>' if p.get("email") else ""

    st.markdown(f"""
    <div class="hero">
        <div class="hero-name" style="font-size: 1.7rem; font-weight: 800; color:#f0f6fc;"> 👋 Hi, I'm {p['name']}</div>
        <div class="hero-title">🎯 {p['title']}</div>
        <div class="hero-tagline">{p['tagline']}</div>
        <div style="margin-top:16px;">
            <span class="badge">⚡ Open to Work</span>
            <span class="badge badge-g">🏙 {p['location']}</span>
            <span class="badge badge-p">🎓 Fresher</span>
        </div>
        <div style="margin-top:18px;">{resume_btn}{linkedin_btn}{github_btn}{email_btn}</div>
    </div>""", unsafe_allow_html=True)

    if VISITOR:
        hire_email = f'<a href="mailto:{p["email"]}" class="lb lb-p">✉ Email Me</a>' if p.get("email") else ""
        hire_li = f'<a href="{p["linkedin"]}" target="_blank" class="lb">💼 LinkedIn</a>' if p.get("linkedin") else ""
        hire_cv = f'<a href="{p["resume_link"]}" target="_blank" class="lb">📄 Resume</a>' if p.get("resume_link") else ""
        st.markdown(f"""
        <div class="hb">
            <div>
                <div style="font-weight:700;color:#2563eb;font-size:1rem;">👋 Thanks for visiting!</div>
                <div style="color:#1e293b;font-size:1.3rem;margin-top:4px;">I'm actively looking for Data Engineer roles — feel free to reach out.</div>
            </div>
            <div style="margin-top:10px;">{hire_email}{hire_li}{hire_cv}</div>
        </div>""", unsafe_allow_html=True)

    projs = data["projects"]
    c1, c2, c3 = st.columns(3)
    for col, num, lbl in zip(
        [c1, c2, c3],
        [len(projs), sum(len(v) for v in data["skills"].values()), len(data["certifications"])],
        ["Projects", "Skills", "Certifications"]
    ):
        with col:
            st.markdown(f'<div class="sb"><div class="sn">{num}</div><div class="sl">{lbl}</div></div>', unsafe_allow_html=True)

    featured = [x for x in projs if x.get("highlight")]
    if featured:
        st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#2563eb; margin-bottom:16px;">🌟 Featured Projects</div>', unsafe_allow_html=True)
        cols = st.columns(min(len(featured), 2))
        for i, pr in enumerate(featured[:4]):
            tech_html = "".join([f'<span class="sp">{t}</span>' for t in pr["tech"][:5]])
            gh_btn = f'<a href="{pr["github"]}" target="_blank" class="lb">🐙 GitHub</a>' if pr.get("github") else ""
            dm_btn = f'<a href="{pr["demo"]}" target="_blank" class="lb">🌐 Demo</a>' if pr.get("demo") else ""
            links_html = f'<div style="border-top:1px solid #30363d;padding-top:12px;margin-top:8px;display:flex;gap:8px;">{gh_btn}{dm_btn}</div>' if (pr.get("github") or pr.get("demo")) else ""
            with cols[i % len(cols)]:
                st.markdown(f"""
                <div style="background:linear-gradient(160deg,#161b22 0%,#1c2333 100%);
                            border:1px solid #30363d;border-top:3px solid #58a6ff;
                            border-radius:14px;padding:22px 20px 16px;margin-bottom:16px;
                            box-shadow:0 0 40px rgba(88,166,255,0.18),0 4px 20px rgba(0,0,0,0.5);
                            position:relative;overflow:hidden;">
                    <div style="position:absolute;top:0;right:0;width:110px;height:110px;
                                background:radial-gradient(circle at top right,rgba(88,166,255,0.13),transparent 65%);
                                pointer-events:none;"></div>
                    <div style="position:absolute;top:12px;left:-1px;width:3px;height:44px;
                                background:linear-gradient(180deg,#58a6ff,transparent);border-radius:0 2px 2px 0;"></div>
                    <div style="font-weight:800;color:#e6edf3;font-size:1.05rem;letter-spacing:-0.3px;
                                line-height:1.35;margin-bottom:12px;">{pr['title']}</div>
                    <div style="font-size:0.85rem;color:#8b949e;margin-bottom:14px;line-height:1.8;">{pr['description']}</div>
                    <div style="margin-bottom:16px;display:flex;flex-wrap:wrap;gap:5px;">{tech_html}</div>
                    {links_html}
                </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#2563eb; margin-bottom:16px;">🛠 Skills</div>', unsafe_allow_html=True)
    skill_cols = st.columns(3)
    for i, (cat, skills) in enumerate(data["skills"].items()):
        with skill_cols[i % 3]:
            pills = "".join([f'<span class="sp">{s}</span>' for s in skills])
            st.markdown(f'<div class="card"><div style="font-weight:600;color:#58a6ff;font-size:0.85rem;margin-bottom:8px;">{cat}</div>{pills}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#2563eb; margin-bottom:16px;">🏅 Certifications</div>', unsafe_allow_html=True)
    home_cert_cols = st.columns(4)
    for i, cert in enumerate(data["certifications"]):
        link_url = cert.get("link", "")
        arrow = ' <span style="color:#58a6ff;font-size:0.66rem;">↗</span>' if link_url else ""
        with home_cert_cols[i % 4]:
            if link_url:
                st.markdown(f"""<a href="{link_url}" target="_blank" style="text-decoration:none;display:block;">
                <div style="background:#161b22;border:1px solid #21262d;border-radius:8px;
                            padding:10px 12px;margin-bottom:10px;display:flex;align-items:center;gap:10px;cursor:pointer;"
                     onmouseover="this.style.borderColor='#58a6ff';this.style.boxShadow='0 0 12px rgba(88,166,255,0.25)';this.style.background='#1c2333'"
                     onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none';this.style.background='#161b22'">
                    <div style="font-size:1.1rem;flex-shrink:0;">🏅</div>
                    <div style="overflow:hidden;">
                        <div style="font-weight:600;color:#e6edf3;font-size:0.78rem;line-height:1.3;
                                    white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert["name"]}{arrow}</div>
                        <div style="color:#58a6ff;font-size:0.7rem;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert["issuer"]}</div>
                        <div style="color:#8b949e;font-size:0.68rem;margin-top:1px;">{cert["year"]}</div>
                    </div>
                </div></a>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background:#161b22;border:1px solid #21262d;border-radius:8px;
                            padding:10px 12px;margin-bottom:10px;display:flex;align-items:center;gap:10px;">
                    <div style="font-size:1.1rem;flex-shrink:0;">🏅</div>
                    <div style="overflow:hidden;">
                        <div style="font-weight:600;color:#e6edf3;font-size:0.78rem;line-height:1.3;
                                    white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert["name"]}</div>
                        <div style="color:#58a6ff;font-size:0.7rem;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert["issuer"]}</div>
                        <div style="color:#8b949e;font-size:0.68rem;margin-top:1px;">{cert["year"]}</div>
                    </div>
                </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════════════════
elif page == "about":
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">👤 About Me</div>', unsafe_allow_html=True)
    email_link = f'<a href="mailto:{p["email"]}" class="lb">✉ {p["email"]}</a>' if p.get("email") else ""
    phone_badge = f'<span class="badge">📞 {p["phone"]}</span>' if p.get("phone") else ""
    st.markdown(f"""
    <div class="card">
        <div style="font-size:0.97rem;color:#c9d1d9;line-height:1.9;">{p['about']}</div>
        <div style="margin-top:18px;color:#8b949e;font-size:0.85rem;margin-bottom:6px;">📬 Contact</div>
        <div>{email_link}{phone_badge}</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">🔗 Find Me Online</div>', unsafe_allow_html=True)
    platforms = [
        ("💼", "LinkedIn", "Connect professionally", p.get("linkedin")),
        ("🐙", "GitHub", "Browse my code", p.get("github")),
        ("📄", "Resume", "Download / View", p.get("resume_link")),
        # ("💻", "LeetCode", "DSA solutions", p.get("leetcode")),
        # ("📊", "Kaggle", "Data science notebooks", p.get("kaggle")),
        # ("📝", "Medium", "Technical blogs", p.get("medium")),
    ]
    pc = st.columns(3)
    for i, (icon, name, desc, url) in enumerate(platforms):
        with pc[i % 3]:
            if url:
                st.markdown(f'<div class="card" style="text-align:center;"><div style="font-size:1.4rem;">{icon}</div><div style="font-weight:600;color:#e6edf3;margin:6px 0 4px;">{name}</div><div style="font-size:0.8rem;color:#8b949e;margin-bottom:12px;">{desc}</div><a href="{url}" target="_blank" class="lb">Visit ↗</a></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="card" style="text-align:center;opacity:0.4;"><div style="font-size:1.4rem;">{icon}</div><div style="font-weight:600;color:#e6edf3;margin:6px 0 4px;">{name}</div><div style="font-size:0.8rem;color:#8b949e;margin-bottom:8px;">{desc}</div><div style="font-size:0.74rem;color:#8b949e;">Not configured</div></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════════════════
elif page == "experience":
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">💼 Work Experience</div>', unsafe_allow_html=True)
    for exp in data["experience"]:
        pts_html = "".join([f'<li style="color:#334155;font-size:0.9rem;margin-bottom:5px;">{pt}</li>' for pt in exp["points"]])
        st.markdown(f"""
        <div class="tl">
            <div style="font-weight:700;color:#1e293b;font-size:1.15rem;">{exp['role']}</div>
            <div style="color:#2563eb;font-size:1.0rem;">{exp['company']}</div>
            <div style="color:#64748b;font-size:0.85rem;margin:2px 0 10px;">📅 {exp['duration']} · 📍 {exp['location']}</div>
            <ul style="padding-left:18px;margin:0;">{pts_html}</ul>
        </div>""", unsafe_allow_html=True)

        if not VISITOR:
            with st.expander(f"✏️ Edit: {exp['role']} @ {exp['company']}"):
                role    = st.text_input("Role",     exp["role"],     key=f"er_{exp['id']}")
                co      = st.text_input("Company",  exp["company"],  key=f"ec_{exp['id']}")
                dur     = st.text_input("Duration", exp["duration"], key=f"ed_{exp['id']}")
                loc_exp = st.text_input("Location", exp["location"], key=f"el_{exp['id']}")
                pts_raw = st.text_area("Bullet points (one per line)", "\n".join(exp["points"]), height=120, key=f"ep_{exp['id']}")
                bc1, bc2 = st.columns(2)
                with bc1:
                    if st.button("💾 Save", key=f"es_{exp['id']}"):
                        for idx, e in enumerate(data["experience"]):
                            if e["id"] == exp["id"]:
                                data["experience"][idx].update({"role": role, "company": co, "duration": dur, "location": loc_exp, "points": [l.strip() for l in pts_raw.split("\n") if l.strip()]})
                        save_data(data); st.success("Saved!"); st.rerun()
                with bc2:
                    arm = f"arm_exp_{exp['id']}"
                    if st.session_state.get(arm):
                        if st.button("⚠️ Confirm Delete", key=f"ecd_{exp['id']}"):
                            data["experience"] = [e for e in data["experience"] if e["id"] != exp["id"]]
                            save_data(data); st.session_state[arm] = False; st.rerun()
                    else:
                        if st.button("🗑 Delete", key=f"edl_{exp['id']}"):
                            st.session_state[arm] = True; st.rerun()

    if not VISITOR:
        st.markdown('<div class="sh">➕ Add Experience</div>', unsafe_allow_html=True)
        with st.expander("Add new experience"):
            nr = st.text_input("Role", key="ne_role")
            nc = st.text_input("Company", key="ne_co")
            nd = st.text_input("Duration (e.g. Jun 2024 – Aug 2024)", key="ne_dur")
            nl = st.text_input("Location", key="ne_loc")
            np_raw = st.text_area("Bullet points (one per line)", height=100, key="ne_pts")
            if st.button("➕ Add Experience"):
                if nr.strip():
                    data["experience"].append({"id": next_id(data["experience"]), "role": nr, "company": nc, "duration": nd, "location": nl, "points": [l.strip() for l in np_raw.split("\n") if l.strip()]})
                    save_data(data); st.success("Added!"); st.rerun()
                else:
                    st.warning("Role is required.")

# ════════════════════════════════════════════════════════════
# PROJECTS
# ════════════════════════════════════════════════════════════
elif page == "projects":
    # 1. Global CSS fix: Forces all expander header titles on this page to be highly visible bright silver-white
    st.markdown("""
        <style>
        .stExpander p {
            color: #f0f6fc;
            font-weight: 700;
            font-size: 1.05rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main page header: Fixed to stand out beautifully against your dark background
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#58a6ff; margin-bottom:16px;">🚀 Projects</div>', unsafe_allow_html=True)

    projs = data["projects"]

    # Status summary — owner only
    if not VISITOR:
        s1, s2, s3, s4 = st.columns(4)
        for col, lbl in zip([s1, s2, s3, s4], ["Completed", "In Progress", "Planning", "On Hold"]):
            cnt = sum(1 for x in projs if x["status"] == lbl)
            col.markdown(f'<div class="sb" style="border-color:{STATUS_COLOR.get(lbl,"")}40;"><div class="sn" style="color:{STATUS_COLOR.get(lbl,"")};font-size:1.4rem;">{cnt}</div><div class="sl" style="color:#8b949e;">{lbl}</div></div>', unsafe_allow_html=True)
        st.markdown("")

    for pr in projs:
        is_hl = pr.get("highlight", False)
        tech_html = "".join([f'<span class="sp">{t}</span>' for t in pr["tech"]])
        gh_btn = f'<a href="{pr["github"]}" target="_blank" class="lb">🐙 GitHub</a>' if pr.get("github") else ""
        dm_btn = f'<a href="{pr["demo"]}" target="_blank" class="lb">🌐 Demo</a>' if pr.get("demo") else ""
        links_row = f'<div style="border-top:1px solid #30363d;padding-top:12px;margin-top:6px;display:flex;gap:8px;flex-wrap:wrap;">{gh_btn}{dm_btn}</div>' if (pr.get("github") or pr.get("demo")) else ""
        hl_badge = '<span style="background:rgba(88,166,255,0.15);color:#58a6ff;border:1px solid rgba(88,166,255,0.4);border-radius:20px;padding:2px 10px;font-size:0.7rem;font-weight:700;">⭐ Featured</span>' if is_hl else ""
        glow = "box-shadow:0 0 40px rgba(88,166,255,0.18),0 4px 20px rgba(0,0,0,0.5);" if is_hl else "box-shadow:0 2px 10px rgba(0,0,0,0.3);"
        bg   = "background:linear-gradient(160deg,#161b22 0%,#1c2333 100%);" if is_hl else "background:#161b22;"
        hl_strip = '<div style="position:absolute;top:12px;left:-1px;width:3px;height:44px;background:linear-gradient(180deg,#58a6ff,transparent);border-radius:0 2px 2px 0;"></div>' if is_hl else ""

        label = f"{'⭐ ' if is_hl else ''}{pr['title']}"
        with st.expander(label, expanded=is_hl):
            st.markdown(f"""
            <div style="{bg}border:1px solid #30363d;border-top:3px solid #58a6ff;{glow}
                        border-radius:14px;padding:22px 20px 16px;position:relative;overflow:hidden;margin-bottom:6px;">
                <div style="position:absolute;top:0;right:0;width:110px;height:110px;
                            background:radial-gradient(circle at top right,rgba(88,166,255,0.1),transparent 65%);
                            pointer-events:none;"></div>
                {hl_strip}
                <div style="display:flex;justify-content:space-between;align-items:flex-start;
                            margin-bottom:12px;gap:10px;flex-wrap:wrap;">
                    <div style="font-weight:800;color:#e6edf3;font-size:1.05rem;
                                letter-spacing:-0.3px;line-height:1.35;flex:1;">{pr['title']}</div>
                    {hl_badge}
                </div>
                <div style="font-size:0.88rem;color:#8b949e;margin-bottom:16px;line-height:1.8;">{pr['description']}</div>
                <div style="margin-bottom:16px;display:flex;flex-wrap:wrap;gap:5px;">{tech_html}</div>
                {links_row}
            </div>""", unsafe_allow_html=True)

            # Task checklist — owner only
            if not VISITOR:
                st.markdown("---")
                st.markdown("**📋 Task Checklist**")
                tasks = pr.get("tasks", [])
                done_n = sum(1 for t in tasks if t["done"])
                st.markdown(f'<div style="font-size:0.8rem;color:#8b949e;margin-bottom:8px;">{done_n} of {len(tasks)} done</div>', unsafe_allow_html=True)

                pr_idx = next((i for i, x in enumerate(data["projects"]) if x["id"] == pr["id"]), None)
                for ti, task in enumerate(tasks):
                    tc1, tc2 = st.columns([8, 1])
                    with tc1:
                        new_done = st.checkbox(task["task"], value=task["done"], key=f"task_{pr['id']}_{ti}")
                        if new_done != task["done"] and pr_idx is not None:
                            data["projects"][pr_idx]["tasks"][ti]["done"] = new_done
                            save_data(data); st.rerun()
                    with tc2:
                        if st.button("✕", key=f"deltask_{pr['id']}_{ti}", help="Remove task") and pr_idx is not None:
                            data["projects"][pr_idx]["tasks"].pop(ti)
                            save_data(data); st.rerun()

                new_task_txt = st.text_input("Add task", key=f"nt_{pr['id']}", placeholder="e.g. Write unit tests")
                if st.button("➕ Add Task", key=f"at_{pr['id']}") and pr_idx is not None:
                    if new_task_txt.strip():
                        data["projects"][pr_idx]["tasks"].append({"task": new_task_txt.strip(), "done": False})
                        save_data(data); st.rerun()

                # Edit project fields
                st.markdown("---")
                st.markdown("**✏️ Edit Project**")
                e1, e2, e3 = st.columns(3)
                with e1:
                    new_status = st.selectbox("Status", ["Completed", "In Progress", "Planning", "On Hold"],
                        index=["Completed", "In Progress", "Planning", "On Hold"].index(pr["status"]), key=f"ps_{pr['id']}")
                with e2:
                    new_prog = st.slider("Progress %", 0, 100, int(pr["progress"]), key=f"pp_{pr['id']}")
                with e3:
                    new_hl = st.checkbox("⭐ Feature on Home", value=pr.get("highlight", False), key=f"ph_{pr['id']}")

                new_title = st.text_input("Title", pr["title"], key=f"ptitle_{pr['id']}")
                new_desc  = st.text_area("Description", pr["description"], height=70, key=f"pdesc_{pr['id']}")
                new_tech  = st.text_input("Tech stack (comma-separated)", ", ".join(pr["tech"]), key=f"ptech_{pr['id']}")
                new_gh    = st.text_input("GitHub URL", pr.get("github", ""), key=f"pgh_{pr['id']}")
                new_demo  = st.text_input("Demo URL", pr.get("demo", ""), key=f"pdemo_{pr['id']}")
                new_cat   = st.text_input("Category", pr.get("category", ""), key=f"pcat_{pr['id']}")

                b1, b2 = st.columns([3, 1])
                with b1:
                    if st.button("💾 Save Changes", key=f"psave_{pr['id']}"):
                        if pr_idx is not None:
                            data["projects"][pr_idx].update({
                                "title": new_title, "description": new_desc,
                                "tech": [t.strip() for t in new_tech.split(",") if t.strip()],
                                "github": new_gh, "demo": new_demo, "category": new_cat,
                                "status": new_status, "progress": new_prog, "highlight": new_hl
                            })
                            if new_status == "Completed" and new_prog == 100:
                                from datetime import date
                                data["projects"][pr_idx]["completed"] = str(date.today())
                            save_data(data); st.success("✅ Saved!"); st.rerun()
                with b2:
                    arm = f"arm_del_{pr['id']}"
                    if st.session_state.get(arm):
                        if st.button("⚠️ Confirm", key=f"pcd_{pr['id']}"):
                            data["projects"] = [x for x in data["projects"] if x["id"] != pr["id"]]
                            save_data(data); st.session_state[arm] = False; st.rerun()
                        st.caption("confirm?")
                    else:
                        if st.button("🗑 Delete", key=f"pdel_{pr['id']}"):
                            st.session_state[arm] = True; st.rerun()

    if not VISITOR:
        st.markdown('<div style="color: #58a6ff; font-weight: 600; font-size: 1.05rem; margin-bottom: 12px;">%s</div>' % "➕ Add New Project", unsafe_allow_html=True)
        with st.expander("Add a new project"):
            a1, a2 = st.columns(2)
            with a1:
                at   = st.text_input("Title", key="apt")
                ad   = st.text_area("Description", height=80, key="apd")
                atc  = st.text_input("Tech stack (comma-separated)", key="aptc")
            with a2:
                agh  = st.text_input("GitHub URL", key="apgh")
                adm  = st.text_input("Demo URL (optional)", key="apdm")
                acat = st.text_input("Category (e.g. Streaming, Cloud, ETL)", key="apcat")
                ast_ = st.selectbox("Status", ["Planning", "In Progress", "Completed", "On Hold"], key="apst")
                apr_ = st.slider("Progress %", 0, 100, 0, key="appr")
                ahl  = st.checkbox("⭐ Feature on Home", key="aphl")
            if st.button("➕ Add Project"):
                if at.strip():
                    from datetime import date
                    data["projects"].append({
                        "id": next_id(data["projects"]), "title": at, "description": ad,
                        "tech": [t.strip() for t in atc.split(",") if t.strip()],
                        "github": agh, "demo": adm, "status": ast_, "progress": apr_,
                        "tasks": [], "highlight": ahl, "category": acat,
                        "started": str(date.today()), "completed": ""
                    })
                    save_data(data); st.success("✅ Project added!"); st.rerun()
                else:
                    st.warning("Title is required.")

# ════════════════════════════════════════════════════════════
# SKILLS
# ════════════════════════════════════════════════════════════
elif page == "skills":
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">🛠 Technical Skills</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.85rem;color:#8b949e;margin:-10px 0 18px;"><span style="color:#58a6ff;font-weight:600;">Blue highlighted</span> skills are proved by a project · hover to see which one · grey = listed skill</div>', unsafe_allow_html=True)

    for cat, skills in data["skills"].items():
        pills_html = ""
        for skill in skills:
            linked = get_projects_for_skill(skill)
            if linked:
                proj_names = " | ".join(pr["title"] for pr in linked)
                pills_html += f'<span class="sp sp-proved" title="Proved in: {proj_names}">✓ {skill}</span>'
            else:
                pills_html += f'<span class="sp">{skill}</span>'

        st.markdown(f"""
        <div class="card">
            <div style="font-weight:700;color:#58a6ff;margin-bottom:12px;font-size:0.93rem;">⚙ {cat}</div>
            <div>{pills_html}</div>
        </div>""", unsafe_allow_html=True)

    if not VISITOR:
        unproven = [(cat, s) for cat, skills in data["skills"].items() for s in skills if not get_projects_for_skill(s)]
        if unproven:
            st.markdown('<div class="sh">⚠️ Skills Without Project Proof</div>', unsafe_allow_html=True)
            st.markdown('<div style="color:#8b949e;font-size:0.87rem;margin:-10px 0 14px;">Add a project using these skills to make your portfolio stronger.</div>', unsafe_allow_html=True)
            pills = "".join([f'<span class="sp" style="border-color:#f8514940;color:#f85149;">{s}</span>' for _, s in unproven])
            st.markdown(f'<div class="card">{pills}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">🏅 Certifications</div>', unsafe_allow_html=True)
    cert_cols = st.columns(4)
    for i, cert in enumerate(data["certifications"]):
        with cert_cols[i % 4]:
            link_url = cert.get("link", "")
            arrow = ' <span style="color:#58a6ff;font-size:0.66rem;">↗</span>' if link_url else ""
            if link_url:
                st.markdown(f"""<a href="{link_url}" target="_blank" style="text-decoration:none;display:block;">
                <div style="background:#161b22;border:1px solid #21262d;border-radius:8px;
                            padding:10px 12px;margin-bottom:10px;display:flex;align-items:center;gap:10px;cursor:pointer;"
                     onmouseover="this.style.borderColor='#58a6ff';this.style.boxShadow='0 0 12px rgba(88,166,255,0.25)';this.style.background='#1c2333'"
                     onmouseout="this.style.borderColor='#21262d';this.style.boxShadow='none';this.style.background='#161b22'">
                    <div style="font-size:1.1rem;flex-shrink:0;">🏅</div>
                    <div style="overflow:hidden;">
                        <div style="font-weight:600;color:#e6edf3;font-size:0.78rem;line-height:1.3;
                                    white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert['name']}{arrow}</div>
                        <div style="color:#58a6ff;font-size:0.7rem;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert['issuer']}</div>
                        <div style="color:#8b949e;font-size:0.68rem;margin-top:1px;">{cert['year']}</div>
                    </div>
                </div></a>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background:#161b22;border:1px solid #21262d;border-radius:8px;
                            padding:10px 12px;margin-bottom:10px;display:flex;align-items:center;gap:10px;">
                    <div style="font-size:1.1rem;flex-shrink:0;">🏅</div>
                    <div style="overflow:hidden;">
                        <div style="font-weight:600;color:#e6edf3;font-size:0.78rem;line-height:1.3;
                                    white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert['name']}</div>
                        <div style="color:#58a6ff;font-size:0.7rem;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{cert['issuer']}</div>
                        <div style="color:#8b949e;font-size:0.68rem;margin-top:1px;">{cert['year']}</div>
                    </div>
                </div>""", unsafe_allow_html=True)

            if not VISITOR:
                with st.expander("✏️ Edit"):
                    cn = st.text_input("Name",   cert["name"],         key=f"cn_{cert['id']}")
                    ci = st.text_input("Issuer", cert["issuer"],       key=f"ci_{cert['id']}")
                    cy = st.text_input("Year",   cert["year"],         key=f"cy_{cert['id']}")
                    cl = st.text_input("Link",   cert.get("link", ""), key=f"cl_{cert['id']}")
                    sc1, sc2 = st.columns(2)
                    with sc1:
                        if st.button("💾 Save", key=f"cs_{cert['id']}"):
                            for j, c in enumerate(data["certifications"]):
                                if c["id"] == cert["id"]:
                                    data["certifications"][j].update({"name": cn, "issuer": ci, "year": cy, "link": cl})
                            save_data(data); st.success("Saved!"); st.rerun()
                    with sc2:
                        arm = f"arm_cert_{cert['id']}"
                        if st.session_state.get(arm):
                            if st.button("⚠️ Confirm", key=f"ccd_{cert['id']}"):
                                data["certifications"] = [c for c in data["certifications"] if c["id"] != cert["id"]]
                                save_data(data); st.session_state[arm] = False; st.rerun()
                        else:
                            if st.button("🗑 Delete", key=f"cdl_{cert['id']}"):
                                st.session_state[arm] = True; st.rerun()

    if not VISITOR:
        st.markdown('<div class="sh">➕ Add Certification</div>', unsafe_allow_html=True)
        with st.expander("Add certification"):
            acn = st.text_input("Certificate Name", key="acn")
            aci = st.text_input("Issuer", key="aci")
            acy = st.text_input("Year", key="acy")
            acl = st.text_input("Verify Link (optional)", key="acl")
            if st.button("➕ Add Certification"):
                if acn.strip():
                    data["certifications"].append({"id": next_id(data["certifications"]), "name": acn, "issuer": aci, "year": acy, "link": acl})
                    save_data(data); st.success("Added!"); st.rerun()
                else:
                    st.warning("Name is required.")

# ════════════════════════════════════════════════════════════
# EDUCATION
# ════════════════════════════════════════════════════════════
elif page == "education":
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">🎓 Education</div>', unsafe_allow_html=True)

    for edu in data["education"]:
        hl = "".join([f'<li style="color:#334155; font-size:0.92rem; margin-bottom:6px; line-height:1.5;">{h}</li>' for h in edu.get("highlights", [])])
        st.markdown(f"""
        <div class="card card-hl" style="background-color: #f8fafc; 
                                        border: 1px solid #e2e8f0; 
                                        border-left: 5px solid #2563eb; 
                                        padding: 20px; 
                                        border-radius: 8px; 
                                        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); 
                                        margin-bottom: 24px;">
           <div style="font-weight:700; color:#0f172a; font-size:1.15rem;">{edu['degree']}</div>
            <div style="color:#2563eb; font-weight:600; font-size:1.0rem; margin:6px 0 4px;">🏛 {edu['institution']}</div>
            <div style="color:#64748b; font-size:0.88rem; margin-bottom:12px; font-weight:500;">📅 {edu['year']} · 🎯 {edu['score']}</div>
            <ul style="padding-left:20px; margin:0;">{hl}</ul>
        </div>""", unsafe_allow_html=True)

        if not VISITOR:
            with st.expander(f"✏️ Edit: {edu['degree']}"):
                ed  = st.text_input("Degree",      edu["degree"],      key=f"edd_{edu['id']}")
                ei  = st.text_input("Institution", edu["institution"], key=f"edi_{edu['id']}")
                ey  = st.text_input("Year",        edu["year"],        key=f"edy_{edu['id']}")
                es  = st.text_input("Score/CGPA",  edu["score"],       key=f"eds_{edu['id']}")
                eh  = st.text_area("Highlights (one per line)", "\n".join(edu.get("highlights", [])), height=100, key=f"edh_{edu['id']}")
                ec1, ec2 = st.columns(2)
                with ec1:
                    if st.button("💾 Save", key=f"edu_save_{edu['id']}"):
                        for j, e in enumerate(data["education"]):
                            if e["id"] == edu["id"]:
                                data["education"][j].update({"degree": ed, "institution": ei, "year": ey, "score": es, "highlights": [l.strip() for l in eh.split("\n") if l.strip()]})
                        save_data(data); st.success("Saved!"); st.rerun()
                with ec2:
                    arm = f"arm_edu_{edu['id']}"
                    if st.session_state.get(arm):
                        if st.button("⚠️ Confirm", key=f"edu_cd_{edu['id']}"):
                            data["education"] = [e for e in data["education"] if e["id"] != edu["id"]]
                            save_data(data); st.session_state[arm] = False; st.rerun()
                    else:
                        if st.button("🗑 Delete", key=f"edu_del_{edu['id']}"):
                            st.session_state[arm] = True; st.rerun()

    if not VISITOR:
        st.markdown('<div class="sh">➕ Add Education</div>', unsafe_allow_html=True)
        with st.expander("Add education"):
            aed = st.text_input("Degree", key="aed")
            aei = st.text_input("Institution", key="aei")
            aey = st.text_input("Year", key="aey")
            aes = st.text_input("Score/CGPA", key="aes")
            aeh = st.text_area("Highlights (one per line)", height=80, key="aeh")
            if st.button("➕ Add Education"):
                if aed.strip():
                    data["education"].append({"id": next_id(data["education"]), "degree": aed, "institution": aei, "year": aey, "score": aes, "highlights": [l.strip() for l in aeh.split("\n") if l.strip()]})
                    save_data(data); st.success("Added!"); st.rerun()
                else:
                    st.warning("Degree is required.")

# ════════════════════════════════════════════════════════════
# ACHIEVEMENTS
# ════════════════════════════════════════════════════════════
elif page == "achievements":
    # Main Page Header: Fixed to high-contrast dark gray for light backgrounds
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">🏆 Achievements & Recognitions</div>', unsafe_allow_html=True)

    for i, ach in enumerate(data["achievements"]):
        icon = "🥇" if i == 0 else "🏆"
        
        # Shared Light-Theme Card Style for achievements
        card_style = """
            background-color: #f8fafc; 
            border: 1px solid #e2e8f0; 
            border-left: 5px solid #f59e0b; /* Premium Amber accent line */
            padding: 16px; 
            border-radius: 8px; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            display: flex; 
            align-items: center; 
            gap: 14px; 
            margin-bottom: 12px;
        """
        # Text style: Deep navy color override
        text_style = "color: #0f172a; font-size: 0.98rem; font-weight: 500;"

        if VISITOR:
            st.markdown(f'<div class="card" style="{card_style}"><div style="font-size:1.5rem;min-width:36px;">{icon}</div><div style="{text_style}">{ach}</div></div>', unsafe_allow_html=True)
        else:
            c1, c2 = st.columns([10, 1])
            with c1:
                st.markdown(f'<div class="card" style="{card_style}"><div style="font-size:1.5rem;min-width:36px;">{icon}</div><div style="{text_style}">{ach}</div></div>', unsafe_allow_html=True)
            with c2:
                arm = f"arm_ach_{i}"
                if st.session_state.get(arm):
                    if st.button("⚠️", key=f"ach_cd_{i}", help="Confirm delete"):
                        data["achievements"].pop(i); save_data(data); st.session_state[arm] = False; st.rerun()
                    st.caption("sure?")
                else:
                    if st.button("🗑", key=f"ach_del_{i}", help="Delete"):
                        st.session_state[arm] = True; st.rerun()

    if not VISITOR:
        st.markdown("---")
        # Sub-header: Forced to dark text to fix the washed-out gray look from the screenshot
        st.markdown('<div class="sh" style="font-size:1.2rem; font-weight:700; color:#1e293b; margin-bottom:12px;">➕ Add Achievement</div>', unsafe_allow_html=True)
        new_ach = st.text_input("Achievement", placeholder="e.g. Solved 200+ DSA problems on LeetCode (Rating: 1500+)")
        if st.button("➕ Add"):
            if new_ach.strip():
                data["achievements"].append(new_ach.strip()); save_data(data); st.success("Added!"); st.rerun()
            else:
                st.warning("Please enter an achievement.")
# ════════════════════════════════════════════════════════════
# RESUME
# ════════════════════════════════════════════════════════════
elif page == "resume":
    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">📄 Resume</div>', unsafe_allow_html=True)
    if p.get("resume_link"):
        st.markdown(f'<div class="rb"><div style="font-weight:700;color:#e6edf3;font-size:1.05rem;margin-bottom:8px;">📄 My Resume</div><div style="color:#8b949e;font-size:0.88rem;margin-bottom:14px;">Hosted on Google Drive. Click to view or download.</div><a href="{p["resume_link"]}" target="_blank" class="lb lb-p">📄 Open Resume ↗</a></div>', unsafe_allow_html=True)
    else:
        st.warning("Resume link not configured. Add it in ⚙️ Edit Profile.")

    st.markdown('<div class="sh" style="font-size:1.4rem; font-weight:700; color:#1e293b; margin-bottom:16px;">📌 Resume Highlights</div>', unsafe_allow_html=True)
    featured = [pr for pr in data["projects"] if pr.get("highlight")]
    skills_flat = [s for v in data["skills"].values() for s in v]
    rc1, rc2 = st.columns(2)
    with rc1:
        rows = "".join([f'<div style="margin-bottom:7px;"><span class="badge badge-g">✓</span> <span style="color:#c9d1d9;font-size:0.9rem;">{pr["title"]}</span></div>' for pr in featured])
        st.markdown(f'<div class="card"><div style="font-weight:700;color:#58a6ff;margin-bottom:10px;">🚀 Featured Projects</div>{rows if rows else "<div style=color:#8b949e;font-size:0.85rem;>No featured projects yet</div>"}</div>', unsafe_allow_html=True)
    with rc2:
        pills = "".join([f'<span class="sp">{s}</span>' for s in skills_flat[:15]])
        st.markdown(f'<div class="card"><div style="font-weight:700;color:#58a6ff;margin-bottom:10px;">🛠 Top Skills</div>{pills}</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# SHARE / LINKS
# ════════════════════════════════════════════════════════════
elif page == "links":
    st.markdown('<div class="sh">🔗 Share Your Portfolio</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="border-color:#58a6ff;">
        <div style="font-weight:700;color:#e6edf3;margin-bottom:14px;">🌐 3 Ways to Go Public</div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;">
            <div style="background:#0d1117;border:1px solid #21262d;border-radius:8px;padding:14px;">
                <div style="color:#58a6ff;font-weight:700;margin-bottom:5px;">🆓 Streamlit Cloud</div>
                <div style="color:#e6edf3;font-size:0.88rem;font-weight:600;">Recommended</div>
                <div style="color:#8b949e;font-size:0.82rem;margin-top:5px;">Free at share.streamlit.io → yourname.streamlit.app</div>
            </div>
            <div style="background:#0d1117;border:1px solid #21262d;border-radius:8px;padding:14px;">
                <div style="color:#3fb950;font-weight:700;margin-bottom:5px;">💡 Railway / Render</div>
                <div style="color:#e6edf3;font-size:0.88rem;font-weight:600;">Free tier available</div>
                <div style="color:#8b949e;font-size:0.82rem;margin-top:5px;">Connect GitHub → deploy in minutes</div>
            </div>
            <div style="background:#0d1117;border:1px solid #21262d;border-radius:8px;padding:14px;">
                <div style="color:#d2a22a;font-weight:700;margin-bottom:5px;">🐙 GitHub Repo</div>
                <div style="color:#e6edf3;font-size:0.88rem;font-weight:600;">Show your code</div>
                <div style="color:#8b949e;font-size:0.82rem;margin-top:5px;">Link the repo on resume — signals you ship code</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sh">📋 Deploy on Streamlit Cloud (5 steps)</div>', unsafe_allow_html=True)
    for step, desc in [
        ("1. Push to GitHub", "Push app.py, requirements.txt, portfolio_data.json to a public GitHub repo."),
        ("2. Go to share.streamlit.io", "Sign in with GitHub. Click New App."),
        ("3. Select your repo", "Choose the repo, branch (main), and set app.py as main file."),
        ("4. Deploy", "You get: https://yourname-portfolio.streamlit.app"),
        ("5. Share the recruiter URL", "Add ?mode=visitor at the end → clean view with no edit buttons."),
    ]:
        st.markdown(f'<div class="card" style="margin-bottom:8px;"><div style="font-weight:700;color:#58a6ff;">{step}</div><div style="color:#8b949e;font-size:0.87rem;margin-top:3px;">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sh">📝 Where to Add Your URL</div>', unsafe_allow_html=True)
    for place, desc in [
        ("📄 Resume", "In the header: Portfolio: yourname.streamlit.app?mode=visitor"),
        ("💼 LinkedIn", "Profile → Edit → Contact info → Website → paste URL"),
        ("🐙 GitHub Profile", "Your profile README.md and pinned repos"),
        ("📧 Email Signature", "Add as clickable link in Gmail / Outlook signature"),
        ("💌 Cold Emails", "End with: 'Portfolio with live projects: [link]'"),
    ]:
        st.markdown(f'<div class="card" style="margin-bottom:8px;"><div style="font-weight:700;color:#e6edf3;">{place}</div><div style="color:#8b949e;font-size:0.85rem;margin-top:3px;">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sh">📦 requirements.txt</div>', unsafe_allow_html=True)
    st.code("streamlit>=1.35.0\npandas>=2.0.0", language="text")

# ════════════════════════════════════════════════════════════
# EDIT PROFILE
# ════════════════════════════════════════════════════════════
elif page == "edit":
    st.markdown('<div class="sh">⚙️ Edit Profile</div>', unsafe_allow_html=True)
    st.info("All changes are saved to portfolio_data.json on your machine.")
    with st.expander("👤 Personal Info", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            data["profile"]["name"]     = st.text_input("Full Name",  p["name"])
            data["profile"]["title"]    = st.text_input("Title",      p["title"])
            data["profile"]["email"]    = st.text_input("Email",      p["email"])
            data["profile"]["phone"]    = st.text_input("Phone",      p["phone"])
            data["profile"]["location"] = st.text_input("Location",   p["location"])
        with c2:
            data["profile"]["linkedin"]    = st.text_input("LinkedIn URL",  p.get("linkedin", ""))
            data["profile"]["github"]      = st.text_input("GitHub URL",    p.get("github", ""))
            data["profile"]["resume_link"] = st.text_input("Resume Link (Google Drive)", p.get("resume_link", ""))
            data["profile"]["leetcode"]    = st.text_input("LeetCode URL",  p.get("leetcode", ""))
            data["profile"]["kaggle"]      = st.text_input("Kaggle URL",    p.get("kaggle", ""))
            data["profile"]["medium"]      = st.text_input("Medium URL",    p.get("medium", ""))
        data["profile"]["tagline"] = st.text_input("Tagline (shown in hero)", p.get("tagline", ""))
        data["profile"]["about"]   = st.text_area("About Me", p.get("about", ""), height=140)

    with st.expander("🛠 Skills"):
        st.markdown("Each category: edit as comma-separated values.")
        for cat in list(data["skills"].keys()):
            val = st.text_area(f"{cat}", ", ".join(data["skills"][cat]), height=68, key=f"sk_{cat}")
            data["skills"][cat] = [s.strip() for s in val.split(",") if s.strip()]
        nc = st.text_input("New category name (type and save)")
        if nc and nc not in data["skills"]:
            data["skills"][nc] = []

    if st.button("💾 Save All Changes", type="primary"):
        save_data(data); st.success("✅ Profile saved!"); st.rerun()
