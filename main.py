# Home / Landing Page — Sri Eshwar College FAQ Bot
# Run with: streamlit run main.py

import streamlit as st

st.set_page_config(
    page_title="Sri Eshwar College — Department FAQ Bot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS (injected on every page via main.py) ────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800&display=swap');

:root {
  --bg-primary:   #0a0e1a;
  --bg-secondary: #0f1628;
  --accent:       #6c63ff;
  --accent-2:     #4ecdc4;
  --accent-3:     #ff6b6b;
  --gold:         #ffd700;
  --text:         #f0f4ff;
  --muted:        #8892b0;
  --border:       rgba(108,99,255,0.2);
}

html, body, [class*="css"] {
  font-family: 'Inter', sans-serif !important;
  background-color: var(--bg-primary) !important;
  color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
  background:
    radial-gradient(ellipse 70% 60% at 10% -5%, rgba(108,99,255,0.22) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 90% 110%, rgba(78,205,196,0.14) 0%, transparent 55%),
    linear-gradient(160deg, #0a0e1a 0%, #0d1526 60%, #0a0e1a 100%);
  padding: 70px 64px 56px;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%236c63ff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/svg%3E");
  pointer-events: none;
}
.hero-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(108,99,255,0.12);
  border: 1px solid rgba(108,99,255,0.35);
  border-radius: 50px;
  padding: 5px 16px;
  font-size: 0.75rem; font-weight: 600;
  color: #a78bfa; letter-spacing: 0.8px;
  text-transform: uppercase; margin-bottom: 22px;
}
.live-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #4ecdc4;
  animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(1.4)} }

.hero-h1 {
  font-family: 'Outfit', sans-serif;
  font-size: clamp(2.4rem, 5vw, 3.8rem);
  font-weight: 800;
  background: linear-gradient(135deg, #fff 0%, #a78bfa 45%, #4ecdc4 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.15; margin: 0 0 10px; letter-spacing: -1px;
}
.hero-sub {
  font-size: 1.05rem; color: var(--muted);
  max-width: 560px; line-height: 1.7; margin: 0 0 36px;
}
.cta-row { display: flex; gap: 14px; flex-wrap: wrap; }
.cta-primary {
  display: inline-flex; align-items: center; gap: 8px;
  background: linear-gradient(135deg, #6c63ff, #4ecdc4);
  color: #fff; font-weight: 700; font-size: 0.92rem;
  padding: 13px 28px; border-radius: 12px;
  border: none; cursor: pointer; text-decoration: none;
  transition: all 0.25s ease; letter-spacing: 0.3px;
  box-shadow: 0 8px 28px rgba(108,99,255,0.35);
}
.cta-primary:hover { transform: translateY(-3px); box-shadow: 0 14px 36px rgba(108,99,255,0.45); }
.cta-secondary {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(108,99,255,0.35);
  color: #a78bfa; font-weight: 600; font-size: 0.92rem;
  padding: 13px 28px; border-radius: 12px;
  cursor: pointer; text-decoration: none;
  transition: all 0.25s ease;
}
.cta-secondary:hover { background: rgba(108,99,255,0.1); transform: translateY(-3px); }

/* ── STATS ── */
.stats-section {
  display: grid; grid-template-columns: repeat(4,1fr);
  gap: 0; border-top: 1px solid rgba(108,99,255,0.15);
  border-bottom: 1px solid rgba(108,99,255,0.15);
}
.stat-box {
  padding: 32px 24px;
  text-align: center;
  border-right: 1px solid rgba(108,99,255,0.12);
  position: relative; overflow: hidden;
  transition: background 0.25s;
}
.stat-box:last-child { border-right: none; }
.stat-box:hover { background: rgba(108,99,255,0.05); }
.stat-num {
  font-family: 'Outfit', sans-serif;
  font-size: 2.6rem; font-weight: 800;
  background: linear-gradient(135deg, #6c63ff, #4ecdc4);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; line-height: 1; margin-bottom: 6px;
}
.stat-lbl { font-size: 0.82rem; color: var(--muted); font-weight: 500; letter-spacing: 0.3px; }

/* ── SECTION LAYOUT ── */
.page-section { padding: 60px 64px; }
.section-eyebrow {
  font-size: 0.7rem; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; color: #6c63ff; margin-bottom: 10px;
}
.section-title {
  font-family: 'Outfit', sans-serif;
  font-size: 2rem; font-weight: 700;
  color: var(--text); margin: 0 0 6px; line-height: 1.25;
}
.section-desc { color: var(--muted); font-size: 0.92rem; line-height: 1.7; max-width: 600px; margin-bottom: 36px; }

/* ── GLASS CARD ── */
.glass-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(108,99,255,0.18);
  border-radius: 20px;
  padding: 28px 24px;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}
.glass-card:hover {
  border-color: rgba(108,99,255,0.38);
  box-shadow: 0 8px 32px rgba(108,99,255,0.12);
  transform: translateY(-4px);
}

/* ── ABOUT GRID ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.about-card-icon { font-size: 2rem; margin-bottom: 14px; }
.about-card-title { font-weight: 700; font-size: 1.05rem; color: var(--text); margin-bottom: 8px; }
.about-card-text { font-size: 0.84rem; color: var(--muted); line-height: 1.65; }

/* ── ACCREDITATION BADGES ── */
.badge-row { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 8px; }
.acc-badge {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 10px 18px; border-radius: 50px;
  font-size: 0.8rem; font-weight: 700; border: 1px solid;
}
.badge-gold  { background: rgba(255,215,0,0.1);  border-color: rgba(255,215,0,0.4);   color: #ffd700; }
.badge-blue  { background: rgba(100,180,255,0.1); border-color: rgba(100,180,255,0.35); color: #64b4ff; }
.badge-green { background: rgba(100,220,100,0.1); border-color: rgba(100,220,100,0.3);  color: #6ddc6d; }
.badge-purple{ background: rgba(167,139,250,0.1); border-color: rgba(167,139,250,0.3);  color: #c4a9ff; }

/* ── HIGHLIGHT CARDS ── */
.highlight-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 18px; }
.hl-card {
  background: rgba(255,255,255,0.035);
  border: 1px solid rgba(108,99,255,0.15);
  border-radius: 16px; padding: 24px 20px;
  text-align: center; transition: all 0.25s ease;
}
.hl-card:hover { border-color: rgba(108,99,255,0.35); transform: translateY(-4px); background: rgba(108,99,255,0.06); }
.hl-icon { font-size: 2.4rem; margin-bottom: 10px; }
.hl-title { font-weight: 700; font-size: 0.9rem; color: var(--text); margin-bottom: 5px; }
.hl-text  { font-size: 0.78rem; color: var(--muted); line-height: 1.55; }

/* ── VISION MISSION ── */
.vm-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.vm-card {
  padding: 32px 28px; border-radius: 20px; position: relative; overflow: hidden;
}
.vm-vision { background: linear-gradient(135deg, rgba(108,99,255,0.12), rgba(108,99,255,0.04)); border: 1px solid rgba(108,99,255,0.28); }
.vm-mission { background: linear-gradient(135deg, rgba(78,205,196,0.10), rgba(78,205,196,0.03)); border: 1px solid rgba(78,205,196,0.28); }
.vm-icon { font-size: 2rem; margin-bottom: 14px; }
.vm-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; }
.vm-vision .vm-label { color: #a78bfa; }
.vm-mission .vm-label { color: #4ecdc4; }
.vm-title { font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 12px; }
.vm-text  { font-size: 0.84rem; color: var(--muted); line-height: 1.7; }

/* ── FOOTER CTA BANNER ── */
.footer-cta {
  background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(78,205,196,0.08));
  border: 1px solid rgba(108,99,255,0.25);
  border-radius: 24px; padding: 48px 40px;
  text-align: center; margin: 0 64px 64px;
}
.footer-cta h2 {
  font-family: 'Outfit', sans-serif; font-size: 1.8rem; font-weight: 800;
  color: var(--text); margin: 0 0 10px;
}
.footer-cta p { color: var(--muted); font-size: 0.9rem; margin: 0 0 26px; }

/* Divider */
.hdivider { height:1px; background: linear-gradient(90deg,transparent,rgba(108,99,255,0.3),transparent); margin: 0 64px; }

/* Streamlit page links */
a[data-testid="stPageLink-NavLink"] {
  color: var(--text) !important;
  text-decoration: none !important;
  background: transparent !important;
}

/* Sidebar */
[data-testid="stSidebar"] { background: rgba(10,14,26,0.97) !important; border-right: 1px solid rgba(108,99,255,0.18) !important; }
[data-testid="stSidebarNavLink"] { color: var(--text) !important; }
section[data-testid="stSidebar"] a { color: #a78bfa !important; }
</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">
    <div class="live-dot"></div>
    Established 2004 &nbsp;·&nbsp; Coimbatore, Tamil Nadu
  </div>
  <h1 class="hero-h1">Sri Eshwar College<br>of Engineering</h1>
  <p class="hero-sub">
    An autonomous institution affiliated to Anna University, committed to
    excellence in engineering education, research, and innovation — shaping
    future-ready engineers since 2004.
  </p>
  <div class="cta-row">
    <span style="font-size:0.9rem; color:#8892b0; display:flex; align-items:center; gap:6px; padding:13px 0;">
      👇 Use the sidebar or buttons below to explore
    </span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STATS BAR ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-section">
  <div class="stat-box">
    <div class="stat-num">5000+</div>
    <div class="stat-lbl">Students Enrolled</div>
  </div>
  <div class="stat-box">
    <div class="stat-num">300+</div>
    <div class="stat-lbl">Faculty Members</div>
  </div>
  <div class="stat-box">
    <div class="stat-num">95%</div>
    <div class="stat-lbl">Placement Rate</div>
  </div>
  <div class="stat-box">
    <div class="stat-num">20+</div>
    <div class="stat-lbl">Years of Excellence</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── ABOUT SECTION ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-section">
  <div class="section-eyebrow">🏛️ ABOUT US</div>
  <h2 class="section-title">A Legacy of Engineering Excellence</h2>
  <p class="section-desc">
    Sri Eshwar College of Engineering (SECE) is a premier autonomous engineering institution
    located in Coimbatore, Tamil Nadu. Affiliated to Anna University and accredited by NAAC,
    the college offers world-class education across 6 engineering departments.
  </p>
  <div class="about-grid">
    <div class="glass-card">
      <div class="about-card-icon">📍</div>
      <div class="about-card-title">Location & Affiliation</div>
      <div class="about-card-text">
        Strategically located in Coimbatore — the "Manchester of South India." Affiliated to
        <strong style="color:#a78bfa;">Anna University, Chennai</strong>, and approved by AICTE,
        New Delhi.
      </div>
    </div>
    <div class="glass-card">
      <div class="about-card-icon">🎓</div>
      <div class="about-card-title">Autonomous Status</div>
      <div class="about-card-text">
        Granted <strong style="color:#4ecdc4;">Autonomous Status</strong> by Anna University, enabling
        the college to design its own curriculum, conduct independent examinations, and
        award degrees.
      </div>
    </div>
    <div class="glass-card">
      <div class="about-card-icon">🔬</div>
      <div class="about-card-title">Research & Innovation</div>
      <div class="about-card-text">
        Home to multiple funded research labs, industry-collaborated projects, and student
        innovation centres. Over <strong style="color:#ffd700;">100+ patents</strong> filed
        by faculty and students.
      </div>
    </div>
    <div class="glass-card">
      <div class="about-card-icon">🤝</div>
      <div class="about-card-title">Industry Connections</div>
      <div class="about-card-text">
        Strong MoUs with leading companies including <strong style="color:#ff6b6b;">TCS, Wipro,
        Infosys, ZOHO</strong>, and 200+ more, ensuring strong placement support and
        internship opportunities.
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hdivider"></div>', unsafe_allow_html=True)

# ── VISION & MISSION ──────────────────────────────────────────────────────────
st.markdown("""
<div class="page-section">
  <div class="section-eyebrow">🌟 VISION & MISSION</div>
  <h2 class="section-title">What Drives Us</h2>
  <div class="vm-grid">
    <div class="vm-card vm-vision">
      <div class="vm-icon">🔭</div>
      <div class="vm-label">Vision</div>
      <div class="vm-title">To be a globally recognised centre of excellence</div>
      <div class="vm-text">
        To be a premier institution of global repute, committed to producing technically
        competent, morally upright, and socially responsible engineers who contribute to
        the sustainable development of society.
      </div>
    </div>
    <div class="vm-card vm-mission">
      <div class="vm-icon">🎯</div>
      <div class="vm-label">Mission</div>
      <div class="vm-title">Empowering learners through innovation & integrity</div>
      <div class="vm-text">
        To provide quality technical education through innovative teaching-learning
        practices, state-of-the-art infrastructure, industry collaboration, and value-based
        training that prepares students for lifelong success.
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hdivider"></div>', unsafe_allow_html=True)

# ── ACCREDITATIONS ────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-section">
  <div class="section-eyebrow">🏅 ACCREDITATIONS & RANKINGS</div>
  <h2 class="section-title">Recognised for Excellence</h2>
  <p class="section-desc">Our quality and commitment to education is recognised by leading bodies.</p>
  <div class="badge-row">
    <div class="acc-badge badge-gold">⭐ NAAC A+ Accredited</div>
    <div class="acc-badge badge-blue">🏛️ NBA Accredited Depts</div>
    <div class="acc-badge badge-green">✅ ISO 9001:2015 Certified</div>
    <div class="acc-badge badge-purple">📜 AICTE Approved</div>
    <div class="acc-badge badge-gold">🎓 Anna University Autonomous</div>
    <div class="acc-badge badge-blue">🔬 DST-FIST Funded</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hdivider"></div>', unsafe_allow_html=True)

# ── CAMPUS LIFE ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-section">
  <div class="section-eyebrow">🏫 CAMPUS LIFE</div>
  <h2 class="section-title">Life at Sri Eshwar</h2>
  <p class="section-desc">A vibrant campus designed for holistic student development.</p>
  <div class="highlight-grid">
    <div class="hl-card">
      <div class="hl-icon">💻</div>
      <div class="hl-title">World-Class Labs</div>
      <div class="hl-text">State-of-the-art computing labs, embedded systems labs, and innovation centres equipped with the latest hardware and software.</div>
    </div>
    <div class="hl-card">
      <div class="hl-icon">📚</div>
      <div class="hl-title">Central Library</div>
      <div class="hl-text">A vast library with 50,000+ books, international journals, e-resources, and 24/7 digital access for students and faculty.</div>
    </div>
    <div class="hl-card">
      <div class="hl-icon">🏠</div>
      <div class="hl-title">Hostel & Amenities</div>
      <div class="hl-text">Separate hostels for boys and girls with modern facilities, mess, Wi-Fi, and 24-hour security for a comfortable living experience.</div>
    </div>
    <div class="hl-card">
      <div class="hl-icon">⚽</div>
      <div class="hl-title">Sports & Recreation</div>
      <div class="hl-text">Indoor and outdoor sports facilities including cricket ground, basketball court, gym, and regular inter-college tournaments.</div>
    </div>
    <div class="hl-card">
      <div class="hl-icon">🎭</div>
      <div class="hl-title">Cultural Events</div>
      <div class="hl-text">Annual fests, technical symposiums, hackathons, and cultural events that foster creativity, teamwork, and leadership.</div>
    </div>
    <div class="hl-card">
      <div class="hl-icon">🚌</div>
      <div class="hl-title">Transport Facility</div>
      <div class="hl-text">An extensive fleet of college buses covering major routes across Coimbatore and neighbouring districts for convenient daily commute.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER CTA ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-cta">
  <h2>🚀 Ready to Explore?</h2>
  <p>Dive into department details or jump straight to the AI FAQ chatbot for instant answers.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.page_link("pages/1_🏛️_Departments.py", label="🏛️ Explore Departments", use_container_width=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.page_link("pages/2_🤖_Chatbot.py", label="🤖 Open FAQ Chatbot", use_container_width=True)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
