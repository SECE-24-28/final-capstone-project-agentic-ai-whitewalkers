# Departments Page — Sri Eshwar College FAQ Bot
# Streamlit multi-page app page

import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Departments — Sri Eshwar College",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800&display=swap');

:root {
  --bg-primary: #0a0e1a; --accent: #6c63ff; --accent-2: #4ecdc4;
  --text: #f0f4ff; --muted: #8892b0; --border: rgba(108,99,255,0.2);
}
html, body, [class*="css"] { font-family:'Inter',sans-serif!important; background:var(--bg-primary)!important; color:var(--text)!important; }
#MainMenu,footer,header{visibility:hidden;} .stDeployButton{display:none;}
.block-container{padding:0!important;max-width:100%!important;}

/* PAGE HEADER */
.page-hero {
  background: radial-gradient(ellipse 70% 55% at 50% -10%, rgba(108,99,255,0.2) 0%, transparent 60%),
              linear-gradient(160deg,#0a0e1a 0%,#0d1526 60%,#0a0e1a 100%);
  padding: 50px 64px 40px;
  border-bottom: 1px solid rgba(108,99,255,0.18);
}
.page-eyebrow {
  font-size:.7rem; font-weight:700; letter-spacing:2px;
  text-transform:uppercase; color:#6c63ff; margin-bottom:10px;
}
.page-title {
  font-family:'Outfit',sans-serif; font-size:2.4rem; font-weight:800;
  background:linear-gradient(135deg,#fff 0%,#a78bfa 45%,#4ecdc4 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  margin:0 0 10px; line-height:1.2;
}
.page-desc { color:var(--muted); font-size:.95rem; max-width:580px; line-height:1.7; }

/* DEPT TABS */
.dept-filter { display:flex; gap:10px; flex-wrap:wrap; padding:20px 64px 0; }
.dept-btn {
  padding:8px 20px; border-radius:50px; font-size:.8rem; font-weight:600;
  border:1px solid; cursor:pointer; transition:all .2s;
}

/* DEPT CARD */
.dept-card {
  background:rgba(255,255,255,.038);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border:1px solid rgba(108,99,255,.18);
  border-radius:24px;
  margin:0 64px 28px;
  overflow:hidden;
  transition:all .3s ease;
  display: flex;
  flex-direction: column;
}
.dept-card:hover { 
  border-color:rgba(108,99,255,.4); 
  box-shadow:0 12px 40px rgba(108,99,255,.1); 
  transform: translateY(-4px); 
}
.dept-cover {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-bottom: 1px solid rgba(108,99,255,.18);
}

.dept-header {
  display:flex; align-items:center; gap:20px;
  padding:28px 32px;
  border-bottom:1px solid rgba(108,99,255,.1);
  cursor:pointer;
}
.dept-icon-wrap {
  width:64px; height:64px; border-radius:18px;
  display:flex; align-items:center; justify-content:center;
  font-size:2rem; flex-shrink:0;
}
.dept-name { font-family:'Outfit',sans-serif; font-size:1.3rem; font-weight:700; color:var(--text); margin:0 0 4px; }
.dept-full { font-size:.82rem; color:var(--muted); }
.dept-meta { display:flex; gap:16px; margin-top:8px; }
.dept-tag {
  font-size:.7rem; font-weight:600; padding:3px 10px;
  border-radius:50px; border:1px solid;
}
.dept-body { padding:28px 32px; display:grid; grid-template-columns:1fr 1fr; gap:24px; }

.info-block-title {
  font-size:.68rem; font-weight:700; letter-spacing:1.5px;
  text-transform:uppercase; margin-bottom:12px;
  display:flex; align-items:center; gap:6px;
}
.info-block-title::after { content:''; flex:1; height:1px; background:rgba(108,99,255,.2); }

.info-text { font-size:.84rem; color:var(--muted); line-height:1.7; }
.info-list { list-style:none; padding:0; margin:0; }
.info-list li {
  display:flex; align-items:flex-start; gap:8px;
  padding:6px 0; font-size:.82rem; color:var(--muted);
  border-bottom:1px solid rgba(255,255,255,.04);
}
.info-list li:last-child { border-bottom:none; }
.li-bullet { width:6px; height:6px; border-radius:50%; margin-top:7px; flex-shrink:0; }

/* COURSES TABLE */
.courses-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.course-pill {
  background:rgba(108,99,255,.08); border:1px solid rgba(108,99,255,.2);
  border-radius:10px; padding:10px 14px; font-size:.78rem;
}
.course-pill-label { font-weight:700; color:var(--text); margin-bottom:2px; }
.course-pill-type { font-size:.68rem; color:var(--muted); }

/* ACHIEVEMENT BADGES */
.ach-row { display:flex; gap:10px; flex-wrap:wrap; }
.ach-badge {
  display:inline-flex; align-items:center; gap:6px;
  padding:6px 14px; border-radius:50px;
  font-size:.75rem; font-weight:600; border:1px solid;
}

/* FOOTER CTA */
.dept-footer-cta {
  background:linear-gradient(135deg,rgba(108,99,255,.14),rgba(78,205,196,.08));
  border:1px solid rgba(108,99,255,.25); border-radius:24px;
  padding:44px 40px; text-align:center; margin:40px 64px 60px;
}
.dept-footer-cta h2 { font-family:'Outfit',sans-serif; font-size:1.7rem; font-weight:800; color:var(--text); margin:0 0 10px; }
.dept-footer-cta p  { color:var(--muted); font-size:.9rem; margin:0 0 26px; }

/* Streamlit sidebar */
[data-testid="stSidebar"] { background:rgba(10,14,26,.97)!important; border-right:1px solid rgba(108,99,255,.18)!important; }
</style>
""")

# ── Page Header ───────────────────────────────────────────────────────────────
st.html("""
<div class="page-hero">
  <div class="page-eyebrow">🏛️ ACADEMIC DEPARTMENTS</div>
  <h1 class="page-title">Explore Our Engineering Departments</h1>
  <p class="page-desc">
    Sri Eshwar College of Engineering offers 6 core engineering departments,
    each equipped with cutting-edge labs, experienced faculty, and strong
    industry connections.
  </p>
</div>
""")

st.html("<div style='height:24px'></div>")

# ── Department Data ───────────────────────────────────────────────────────────
departments = [
    {
        "short": "CSE",
        "full": "Computer Science and Engineering",
        "icon": "💻",
        "image": "images/cse.png",
        "color_bg": "rgba(108,99,255,0.18)",
        "color_border": "rgba(108,99,255,0.45)",
        "color_text": "#a78bfa",
        "overview": (
            "The Department of Computer Science and Engineering is the flagship department "
            "of SECE, offering a rigorous curriculum blending core CS fundamentals with "
            "cutting-edge specialisations in AI, ML, cybersecurity, and cloud computing. "
            "Students graduate industry-ready through project-based learning and strong "
            "placement support."
        ),
        "courses": [
            ("B.E. CSE", "UG · 4 Years"),
            ("B.E. CSE (AI & ML)", "UG · 4 Years"),
            ("B.E. CSE (Cyber Security)", "UG · 4 Years"),
            ("M.E. CSE", "PG · 2 Years"),
            ("M.E. Software Engg.", "PG · 2 Years"),
            ("Ph.D. CSE", "Research"),
        ],
        "labs": [
            "Advanced Computing Lab",
            "Data Science & AI Lab",
            "Cyber Security Lab",
            "Cloud & DevOps Lab",
            "IoT & Embedded Systems Lab",
            "Programming Practice Lab",
        ],
        "faculty": "65+ Faculty (15 PhDs)",
        "achievements": ["NBA Accredited", "NIRF Ranked", "Google Dev Club", "Smart India Hackathon Winners"],
        "intake": "480 seats (UG)",
    },
    {
        "short": "ECE",
        "full": "Electronics and Communication Engineering",
        "icon": "📡",
        "image": "images/ece.png",
        "color_bg": "rgba(78,205,196,0.14)",
        "color_border": "rgba(78,205,196,0.4)",
        "color_text": "#4ecdc4",
        "overview": (
            "The ECE department combines strong theoretical foundations with hands-on "
            "practical training in VLSI design, embedded systems, wireless communication, "
            "and signal processing. Students are equipped for careers in hardware design, "
            "telecom, and electronics industries."
        ),
        "courses": [
            ("B.E. ECE", "UG · 4 Years"),
            ("B.E. ECE (IoT)", "UG · 4 Years"),
            ("M.E. Communication Systems", "PG · 2 Years"),
            ("M.E. VLSI Design", "PG · 2 Years"),
            ("Ph.D. ECE", "Research"),
        ],
        "labs": [
            "VLSI & Chip Design Lab",
            "Embedded Systems Lab",
            "RF & Antenna Lab",
            "Digital Signal Processing Lab",
            "Communication Systems Lab",
            "PCB Design Lab",
        ],
        "faculty": "55+ Faculty (12 PhDs)",
        "achievements": ["NBA Accredited", "DST-FIST Funded Lab", "TI University Program", "Best Paper Award — IEEE"],
        "intake": "360 seats (UG)",
    },
    {
        "short": "Mech",
        "full": "Mechanical Engineering",
        "icon": "⚙️",
        "image": "images/mech.png",
        "color_bg": "rgba(255,107,107,0.12)",
        "color_border": "rgba(255,107,107,0.38)",
        "color_text": "#ff6b6b",
        "overview": (
            "The Mechanical Engineering department prepares students for the dynamic "
            "manufacturing, automotive, and aerospace sectors. The curriculum spans "
            "thermodynamics, fluid mechanics, CAD/CAM, robotics, and advanced manufacturing "
            "technologies, supported by well-equipped workshops and design labs."
        ),
        "courses": [
            ("B.E. Mechanical", "UG · 4 Years"),
            ("B.E. Mechatronics", "UG · 4 Years"),
            ("M.E. Manufacturing Engg.", "PG · 2 Years"),
            ("M.E. CAD/CAM", "PG · 2 Years"),
            ("Ph.D. Mechanical", "Research"),
        ],
        "labs": [
            "CAD/CAM Centre",
            "Manufacturing Technology Lab",
            "Thermal & Fluid Lab",
            "Material Testing Lab",
            "Robotics & Automation Lab",
            "3D Printing & Prototyping Lab",
        ],
        "faculty": "48+ Faculty (10 PhDs)",
        "achievements": ["AICTE MODROB Funded", "SAE India Affiliated", "Best Design Project — NATCON", "Industry MoU: TVS Motors"],
        "intake": "240 seats (UG)",
    },
    {
        "short": "EEE",
        "full": "Electrical and Electronics Engineering",
        "icon": "⚡",
        "image": "images/eee.png",
        "color_bg": "rgba(255,215,0,0.10)",
        "color_border": "rgba(255,215,0,0.35)",
        "color_text": "#ffd700",
        "overview": (
            "The EEE department offers a strong grounding in power systems, electrical "
            "machines, control systems, and renewable energy technologies. Students gain "
            "both theoretical and practical expertise through industry-standard equipment, "
            "simulation tools, and real-world project work."
        ),
        "courses": [
            ("B.E. EEE", "UG · 4 Years"),
            ("M.E. Power Systems", "PG · 2 Years"),
            ("M.E. Power Electronics", "PG · 2 Years"),
            ("Ph.D. EEE", "Research"),
        ],
        "labs": [
            "Electrical Machines Lab",
            "Power Electronics Lab",
            "Control Systems Lab",
            "Renewable Energy Lab",
            "PLC & SCADA Lab",
            "High Voltage Lab",
        ],
        "faculty": "40+ Faculty (9 PhDs)",
        "achievements": ["IEI Affiliated Chapter", "TNSCST Funded Projects", "Solar Power Plant — Campus", "Best Intern: BHEL & TNEB"],
        "intake": "180 seats (UG)",
    },
    {
        "short": "Civil",
        "full": "Civil Engineering",
        "icon": "🏗️",
        "image": "images/civil.png",
        "color_bg": "rgba(100,220,100,0.09)",
        "color_border": "rgba(100,220,100,0.32)",
        "color_text": "#6ddc6d",
        "overview": (
            "The Civil Engineering department focuses on structural, environmental, "
            "geotechnical, and transportation engineering. With a strong emphasis on "
            "sustainable construction, smart infrastructure, and GIS-based planning, "
            "graduates are well-equipped for government, private, and research careers."
        ),
        "courses": [
            ("B.E. Civil Engineering", "UG · 4 Years"),
            ("M.E. Structural Engineering", "PG · 2 Years"),
            ("M.E. Environmental Engg.", "PG · 2 Years"),
            ("Ph.D. Civil", "Research"),
        ],
        "labs": [
            "Strength of Materials Lab",
            "Concrete & Highway Lab",
            "Soil Mechanics Lab",
            "Environmental Engg. Lab",
            "Surveying & GIS Lab",
            "Fluid Mechanics Lab",
        ],
        "faculty": "36+ Faculty (8 PhDs)",
        "achievements": ["ICI Student Chapter", "TNSCST Funded Research", "Best Project: CREDAI", "Tie-up: L&T Construction"],
        "intake": "120 seats (UG)",
    },
    {
        "short": "IT",
        "full": "Information Technology",
        "icon": "🖥️",
        "image": "images/it.png",
        "color_bg": "rgba(255,140,0,0.10)",
        "color_border": "rgba(255,140,0,0.32)",
        "color_text": "#ffa040",
        "overview": (
            "The IT department focuses on software development, database management, "
            "networking, and emerging technologies. Students are trained in full-stack "
            "development, cloud computing, and data analytics, with a strong emphasis "
            "on entrepreneurship and startup culture."
        ),
        "courses": [
            ("B.Tech. Information Technology", "UG · 4 Years"),
            ("B.Tech. IT (Data Science)", "UG · 4 Years"),
            ("M.Tech. IT", "PG · 2 Years"),
            ("Ph.D. IT", "Research"),
        ],
        "labs": [
            "Full-Stack Dev Lab",
            "Database Management Lab",
            "Networking & Security Lab",
            "Cloud Computing Lab",
            "Data Analytics Lab",
            "Open Source Projects Lab",
        ],
        "faculty": "42+ Faculty (9 PhDs)",
        "achievements": ["Microsoft Learn Student Ambassador", "IBM SkillBuild Partner", "Top Placement: Zoho & Freshworks", "Best Start-up Idea Award"],
        "intake": "240 seats (UG)",
    }
]

# ── Render Each Department Card ───────────────────────────────────────────────
for dept in departments:
    color_bg     = dept["color_bg"]
    color_border = dept["color_border"]
    color_text   = dept["color_text"]

    # Course pills HTML
    course_pills = ""
    for cname, ctype in dept["courses"]:
        course_pills += f"""
        <div class="course-pill">
          <div class="course-pill-label">{cname}</div>
          <div class="course-pill-type">{ctype}</div>
        </div>"""

    # Labs list HTML
    labs_items = ""
    for lab in dept["labs"]:
        labs_items += f'<li><span class="li-bullet" style="background:{color_text};"></span>{lab}</li>'

    # Achievement badges HTML
    ach_badges = ""
    for ach in dept["achievements"]:
        ach_badges += f'<span class="ach-badge" style="background:{color_bg};border-color:{color_border};color:{color_text};">{ach}</span>'

    # Base64 Image
    img_b64 = get_base64_image(dept.get("image", ""))
    img_html = f'<img src="data:image/png;base64,{img_b64}" class="dept-cover">' if img_b64 else ""

    st.html(f"""
<div class="dept-card">
  {img_html}
  <div class="dept-header">
    <div class="dept-icon-wrap" style="background:{color_bg};border:1px solid {color_border};">
      {dept['icon']}
    </div>
    <div style="flex:1;">
      <div class="dept-name">{dept['full']}</div>
      <div class="dept-full">Department of {dept['full']} &nbsp;·&nbsp; {dept['faculty']}</div>
      <div class="dept-meta">
        <span class="dept-tag" style="background:{color_bg};border-color:{color_border};color:{color_text};">{dept['short']}</span>
        <span class="dept-tag" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:#8892b0;">
          🪑 {dept['intake']}
        </span>
      </div>
    </div>
  </div>

  <div class="dept-body">
    <!-- Overview -->
    <div style="grid-column:1/-1;">
      <div class="info-block-title" style="color:{color_text};">📖 Overview</div>
      <div class="info-text">{dept['overview']}</div>
    </div>

    <!-- Courses -->
    <div>
      <div class="info-block-title" style="color:{color_text};">🎓 Courses Offered</div>
      <div class="courses-grid">{course_pills}</div>
    </div>

    <!-- Labs -->
    <div>
      <div class="info-block-title" style="color:{color_text};">🔬 Labs & Facilities</div>
      <ul class="info-list">{labs_items}</ul>
    </div>

    <!-- Achievements -->
    <div style="grid-column:1/-1;">
      <div class="info-block-title" style="color:{color_text};">🏆 Achievements & Highlights</div>
      <div class="ach-row">{ach_badges}</div>
    </div>
  </div>
</div>
""")

# ── Footer CTA ────────────────────────────────────────────────────────────────
st.html("""
<div class="dept-footer-cta">
  <h2>🤖 Still have questions?</h2>
  <p>
    Our AI-powered FAQ chatbot can answer any department-specific question instantly —
    from syllabus details to exam schedules and placement statistics.
  </p>
</div>
""")

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.page_link("pages/2_🤖_Chatbot.py", label="🤖 Open the FAQ Chatbot", use_container_width=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.page_link("main.py", label="🏠 Back to Home", use_container_width=True)

st.html("<div style='height:40px'></div>")
