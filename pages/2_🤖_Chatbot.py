# Chatbot Page — Sri Eshwar College FAQ Bot
# Streamlit multi-page app — page 2

import streamlit as st
from datetime import datetime as _dt

from rag import setup_vectorstore, chat_chain
from utils import contains_sensitive_topics
from pdf_export import render_pdf_export_button

st.set_page_config(
    page_title="FAQ Chatbot — Sri Eshwar College",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800&display=swap');

:root {
  --bg-primary: #0a0e1a; --accent: #6c63ff; --accent-2: #4ecdc4;
  --text: #f0f4ff; --muted: #8892b0; --border: rgba(108,99,255,0.2);
}
html, body, [class*="css"] { font-family:'Inter',sans-serif!important; background:var(--bg-primary)!important; color:var(--text)!important; }
#MainMenu,footer,header{visibility:hidden;} .stDeployButton{display:none;}
.block-container{padding:0!important;max-width:100%!important;}

/* HERO HEADER */
.chat-hero {
  background:
    radial-gradient(ellipse 80% 60% at 20% -10%, rgba(108,99,255,.18) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 110%, rgba(78,205,196,.12) 0%, transparent 55%),
    linear-gradient(160deg,#0a0e1a 0%,#0d1526 50%,#0a0e1a 100%);
  padding: 28px 48px 20px;
  border-bottom: 1px solid rgba(108,99,255,.15);
  position: relative; overflow: hidden;
}
.chat-hero::before {
  content:''; position:absolute; inset:0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%236c63ff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/svg%3E");
  pointer-events:none;
}
.hero-badge {
  display:inline-flex; align-items:center; gap:6px;
  background:rgba(108,99,255,.12); border:1px solid rgba(108,99,255,.35);
  border-radius:50px; padding:4px 14px; font-size:.75rem; font-weight:600;
  color:#a78bfa; letter-spacing:.5px; margin-bottom:12px;
}
.live-dot { width:7px;height:7px;border-radius:50%;background:#4ecdc4;animation:pulse 2s infinite; }
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.4)}}
.chat-title {
  font-family:'Outfit',sans-serif; font-size:2rem; font-weight:800;
  background:linear-gradient(135deg,#fff 0%,#a78bfa 50%,#4ecdc4 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  margin:0 0 6px; line-height:1.2;
}
.chat-sub { font-size:.92rem; color:var(--muted); margin:0; }

/* DEPT CHIPS */
.dept-chips-bar { display:flex; gap:8px; flex-wrap:wrap; padding:14px 48px 0; }
.dept-chip {
  display:inline-flex; align-items:center; gap:5px;
  padding:5px 14px; border-radius:50px; font-size:.75rem; font-weight:500;
  border:1px solid; cursor:pointer; transition:all .2s ease; white-space:nowrap;
}
.dept-chip:hover { transform:translateY(-2px); filter:brightness(1.2); }

/* STATS BAR */
.stats-bar { display:flex; gap:24px; padding:14px 48px; border-bottom:1px solid rgba(255,255,255,.05); }
.stat-item { display:flex; align-items:center; gap:8px; }
.stat-val  { font-size:.85rem; font-weight:600; color:var(--text); }
.stat-lbl  { font-size:.72rem; color:var(--muted); }

/* CHAT AREA */
.chat-area { padding:24px 48px 12px; max-width:900px; margin:0 auto; }

/* WELCOME CARD */
.welcome-card {
  background:rgba(255,255,255,.03); border:1px solid rgba(108,99,255,.18);
  border-radius:22px; padding:38px 40px; text-align:center; margin:10px auto 28px;
  max-width:660px; backdrop-filter:blur(12px);
}
.welcome-icon { font-size:3.5rem; margin-bottom:14px; display:block; }
.welcome-card h2 { font-family:'Outfit',sans-serif; font-size:1.5rem; font-weight:700; color:var(--text); margin:0 0 10px; }
.welcome-card p  { color:var(--muted); font-size:.88rem; line-height:1.7; margin:0 0 22px; }
.quick-grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; text-align:left; }
.quick-item {
  background:rgba(108,99,255,.08); border:1px solid rgba(108,99,255,.2);
  border-radius:12px; padding:12px 14px; font-size:.8rem; color:#a78bfa;
  transition:all .2s ease;
}
.quick-item:hover { background:rgba(108,99,255,.15); transform:translateY(-2px); }
.quick-item span { display:block; color:var(--muted); font-size:.72rem; margin-top:2px; }

/* MESSAGES */
.msg-wrapper { display:flex; align-items:flex-start; gap:12px; margin-bottom:20px; animation:fadeUp .35s ease; }
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.msg-wrapper.user-msg { flex-direction:row-reverse; }
.avatar { width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0; }
.avatar-bot  { background:linear-gradient(135deg,#6c63ff,#4ecdc4); box-shadow:0 0 16px rgba(108,99,255,.4); }
.avatar-user { background:linear-gradient(135deg,#ff6b6b,#ffa040); box-shadow:0 0 16px rgba(255,107,107,.35); }
.bubble { max-width:72%; padding:14px 18px; border-radius:18px; font-size:.9rem; line-height:1.65; position:relative; }
.bubble-bot  { background:rgba(255,255,255,.055); border:1px solid rgba(108,99,255,.2); border-radius:4px 18px 18px 18px; color:var(--text); backdrop-filter:blur(10px); }
.bubble-user { background:linear-gradient(135deg,rgba(108,99,255,.25),rgba(78,205,196,.15)); border:1px solid rgba(108,99,255,.3); border-radius:18px 4px 18px 18px; color:var(--text); }
.msg-time { font-size:.67rem; color:var(--muted); margin-top:5px; display:block; }

/* INPUT */
.input-wrap { padding:0 48px 28px; max-width:900px; margin:0 auto; }
div[data-testid="stChatInput"] { background:rgba(255,255,255,.04)!important; border:1px solid rgba(108,99,255,.3)!important; border-radius:16px!important; }
div[data-testid="stChatInput"]:focus-within { border-color:rgba(108,99,255,.65)!important; box-shadow:0 0 0 3px rgba(108,99,255,.12)!important; }
div[data-testid="stChatInput"] textarea { background:transparent!important; color:var(--text)!important; font-family:'Inter',sans-serif!important; font-size:.92rem!important; }
div[data-testid="stChatInput"] button { background:linear-gradient(135deg,#6c63ff,#4ecdc4)!important; border-radius:10px!important; border:none!important; }

/* DIVIDER */
.sec-div { height:1px; background:linear-gradient(90deg,transparent,rgba(108,99,255,.3),transparent); margin:0 48px; }

/* SIDEBAR */
[data-testid="stSidebar"] { background:rgba(10,14,26,.97)!important; border-right:1px solid rgba(108,99,255,.18)!important; }
[data-testid="stSidebar"] .stButton>button {
  background:rgba(108,99,255,.12)!important; border:1px solid rgba(108,99,255,.3)!important;
  color:#a78bfa!important; border-radius:10px!important; font-family:'Inter',sans-serif!important;
  font-size:.8rem!important; transition:all .2s ease!important;
}
[data-testid="stSidebar"] .stButton>button:hover { background:rgba(108,99,255,.22)!important; transform:translateX(3px)!important; }
[data-testid="stSidebar"] .stDownloadButton>button { background:linear-gradient(135deg,#6c63ff,#4ecdc4)!important; border:none!important; color:white!important; border-radius:10px!important; font-weight:600!important; }
</style>
""", unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = setup_vectorstore()
if "conversational_chain" not in st.session_state:
    st.session_state.conversational_chain = chat_chain(st.session_state.vectorstore)
if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <style>
    .sb-brand { background:linear-gradient(135deg,rgba(108,99,255,.15),rgba(78,205,196,.08)); border:1px solid rgba(108,99,255,.25); border-radius:16px; padding:20px 18px 16px; margin-bottom:18px; text-align:center; }
    .sb-logo { font-size:2.4rem; margin-bottom:6px; }
    .sb-college { font-family:'Outfit',sans-serif; font-size:1rem; font-weight:700; color:#f0f4ff; margin:0; }
    .sb-tagline { font-size:.7rem; color:#8892b0; margin:4px 0 0; }
    .sb-pills { display:flex; justify-content:center; gap:6px; margin-top:10px; flex-wrap:wrap; }
    .sb-pill { font-size:.65rem; font-weight:600; padding:3px 10px; border-radius:50px; background:rgba(108,99,255,.12); border:1px solid rgba(108,99,255,.3); color:#a78bfa; }
    .sb-hdr { font-size:.67rem; font-weight:700; color:#8892b0; letter-spacing:1.8px; text-transform:uppercase; margin:18px 0 10px; display:flex; align-items:center; gap:6px; }
    .sb-hdr::after { content:''; flex:1; height:1px; background:linear-gradient(90deg,rgba(108,99,255,.3),transparent); }
    .sb-hist-empty { background:rgba(255,255,255,.025); border:1px dashed rgba(108,99,255,.2); border-radius:10px; padding:12px; text-align:center; font-size:.76rem; color:#8892b0; }
    .sb-div { height:1px; background:linear-gradient(90deg,transparent,rgba(108,99,255,.25),transparent); margin:16px 0; }
    </style>
    <div class="sb-brand">
      <div class="sb-logo">🤖</div>
      <p class="sb-college">FAQ Chatbot</p>
      <p class="sb-tagline">Sri Eshwar College · AI Assistant</p>
      <div class="sb-pills">
        <span class="sb-pill">RAG Powered</span>
        <span class="sb-pill">LLaMA 3.1</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation
    st.markdown('<div class="sb-hdr">🗺️ Navigation</div>', unsafe_allow_html=True)
    st.page_link("main.py", label="🏠 Home — College Overview", use_container_width=True)
    st.page_link("pages/1_🏛️_Departments.py", label="🏛️ Departments", use_container_width=True)

    st.markdown('<div class="sb-div"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-hdr">💬 Chat History</div>', unsafe_allow_html=True)

    user_msgs = [
        (idx, msg)
        for idx, msg in enumerate(st.session_state.chat_history)
        if msg["role"] == "user"
    ]
    if not user_msgs:
        st.markdown('<div class="sb-hist-empty">🗨️ No conversations yet.<br>Ask your first question!</div>', unsafe_allow_html=True)
    else:
        for conv_num, (idx, msg) in enumerate(user_msgs, start=1):
            preview = msg["content"][:32] + ("…" if len(msg["content"]) > 32 else "")
            st.button(f"💬 Q{conv_num}: {preview}", key=f"hist_{idx}")

    if st.session_state.chat_history:
        st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)
        if st.button("🗑️ Clear Conversation", key="clear_chat_p2"):
            st.session_state.chat_history = []
            st.session_state.question_count = 0
            st.rerun()

    st.markdown('<div class="sb-div"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-hdr">📄 Export</div>', unsafe_allow_html=True)
    render_pdf_export_button(st.session_state.chat_history)

    st.markdown("""
    <div class="sb-div"></div>
    <div style="text-align:center;font-size:.68rem;color:#8892b0;padding-bottom:6px;">
      Made with ❤️ · Sri Eshwar College<br>
      <span style="color:#6c63ff;">FAQ Bot v2.0</span>
    </div>
    """, unsafe_allow_html=True)

# ── Hero Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-hero">
  <div class="hero-badge"><div class="live-dot"></div> AI POWERED · LIVE</div>
  <h1 class="chat-title">🤖 Department FAQ Chatbot</h1>
  <p class="chat-sub">Ask anything about Sri Eshwar College — academics, admissions, exams, placements, campus & more</p>
</div>
""", unsafe_allow_html=True)

# ── Department Filter Chips ───────────────────────────────────────────────────
st.markdown("""
<div class="dept-chips-bar">
  <div class="dept-chip" style="background:rgba(108,99,255,.12);border-color:rgba(108,99,255,.4);color:#a78bfa;">💻 CSE</div>
  <div class="dept-chip" style="background:rgba(78,205,196,.10);border-color:rgba(78,205,196,.35);color:#4ecdc4;">📡 ECE</div>
  <div class="dept-chip" style="background:rgba(255,107,107,.10);border-color:rgba(255,107,107,.35);color:#ff6b6b;">⚙️ Mechanical</div>
  <div class="dept-chip" style="background:rgba(255,215,0,.10);border-color:rgba(255,215,0,.3);color:#ffd700;">⚡ EEE</div>
  <div class="dept-chip" style="background:rgba(100,220,100,.10);border-color:rgba(100,220,100,.3);color:#6ddc6d;">🏗️ Civil</div>
  <div class="dept-chip" style="background:rgba(255,140,0,.10);border-color:rgba(255,140,0,.3);color:#ffa040;">🖥️ IT</div>
  <div class="dept-chip" style="background:rgba(108,99,255,.06);border-color:rgba(108,99,255,.2);color:#8892b0;">📋 General</div>
</div>
""", unsafe_allow_html=True)

# ── Stats Bar ─────────────────────────────────────────────────────────────────
q_count = st.session_state.question_count
st.markdown(f"""
<div class="stats-bar">
  <div class="stat-item">
    <span style="font-size:1.1rem;">💬</span>
    <div><div class="stat-val">{q_count}</div><div class="stat-lbl">Questions Asked</div></div>
  </div>
  <div class="stat-item">
    <span style="font-size:1.1rem;">🏛️</span>
    <div><div class="stat-val">6</div><div class="stat-lbl">Departments</div></div>
  </div>
  <div class="stat-item">
    <span style="font-size:1.1rem;">⚡</span>
    <div><div class="stat-val">RAG</div><div class="stat-lbl">Knowledge Base</div></div>
  </div>
  <div class="stat-item">
    <span style="font-size:1.1rem;">🧠</span>
    <div><div class="stat-val">LLaMA 3.1</div><div class="stat-lbl">AI Model</div></div>
  </div>
</div>
<div class="sec-div"></div>
""", unsafe_allow_html=True)

# ── Chat Area ─────────────────────────────────────────────────────────────────
st.markdown('<div class="chat-area">', unsafe_allow_html=True)

# Welcome screen
if not st.session_state.chat_history:
    st.markdown("""
    <div class="welcome-card">
      <span class="welcome-icon">🤖</span>
      <h2>Hello! I'm your College FAQ Assistant</h2>
      <p>Ask me anything about Sri Eshwar College departments, admissions,
         syllabus, facilities, faculty, exams, scholarships, and placements.</p>
      <div class="quick-grid">
        <div class="quick-item">📋 Admission Process<span>Eligibility, deadlines & docs</span></div>
        <div class="quick-item">🎓 Academic Programs<span>Courses offered by dept</span></div>
        <div class="quick-item">🏆 Placements<span>Companies, packages & stats</span></div>
        <div class="quick-item">🏫 Campus Facilities<span>Labs, library & hostel</span></div>
        <div class="quick-item">📅 Exam Schedule<span>Internal & university exams</span></div>
        <div class="quick-item">💰 Scholarships<span>Merit & need-based aid</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Render messages
for msg in st.session_state.chat_history:
    role    = msg["role"]
    content = msg["content"]
    ts      = msg.get("timestamp", "")

    if role == "user":
        st.markdown(f"""
<div class="msg-wrapper user-msg">
  <div class="avatar avatar-user">👤</div>
  <div>
    <div class="bubble bubble-user">{content}</div>
    <span class="msg-time" style="text-align:right;">{ts}</span>
  </div>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
<div class="msg-wrapper">
  <div class="avatar avatar-bot">🤖</div>
  <div>
    <div class="bubble bubble-bot">{content}</div>
    <span class="msg-time">{ts}</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Chat Input ────────────────────────────────────────────────────────────────
st.markdown('<div class="input-wrap">', unsafe_allow_html=True)
user_input = st.chat_input("Ask about admissions, departments, exams, placements…")
st.markdown('</div>', unsafe_allow_html=True)

# ── Handle Input ──────────────────────────────────────────────────────────────
if user_input:
    now = _dt.now().strftime("%I:%M %p")

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input,
        "timestamp": now,
    })
    st.session_state.question_count += 1

    if contains_sensitive_topics(user_input):
        assistant_response = (
            "⚠️ It seems your question may be outside my scope. "
            "I'm specifically designed to answer questions about Sri Eshwar College. "
            "Please ask about admissions, academics, departments, campus, or related topics!"
        )
    else:
        raw = st.session_state.conversational_chain({"question": user_input})
        assistant_response = raw["answer"]

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response,
        "timestamp": _dt.now().strftime("%I:%M %p"),
    })
    st.rerun()
