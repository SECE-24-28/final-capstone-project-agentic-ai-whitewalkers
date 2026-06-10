import streamlit as st
from pdf_export import render_pdf_export_button


def render_sidebar():
    """Render the fully redesigned sidebar: branding, stats, history & PDF export."""
    with st.sidebar:

        # ── Sidebar Header / Branding ─────────────────────────────────────────
        st.markdown("""
        <style>
        /* Sidebar branding block */
        .sb-brand {
            background: linear-gradient(135deg,
                rgba(108,99,255,0.15) 0%,
                rgba(78,205,196,0.08) 100%);
            border: 1px solid rgba(108,99,255,0.25);
            border-radius: 16px;
            padding: 20px 18px 16px;
            margin-bottom: 18px;
            text-align: center;
        }
        .sb-logo { font-size: 2.6rem; margin-bottom: 6px; }
        .sb-college {
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: #f0f4ff;
            margin: 0;
            line-height: 1.2;
        }
        .sb-tagline {
            font-size: 0.72rem;
            color: #8892b0;
            margin: 4px 0 0;
            letter-spacing: 0.3px;
        }
        .sb-pills {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin-top: 12px;
            flex-wrap: wrap;
        }
        .sb-pill {
            font-size: 0.67rem;
            font-weight: 600;
            padding: 3px 10px;
            border-radius: 50px;
            background: rgba(108,99,255,0.12);
            border: 1px solid rgba(108,99,255,0.3);
            color: #a78bfa;
            letter-spacing: 0.4px;
        }

        /* Section header */
        .sb-section-hdr {
            font-size: 0.68rem;
            font-weight: 700;
            color: #8892b0;
            letter-spacing: 1.8px;
            text-transform: uppercase;
            margin: 18px 0 10px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .sb-section-hdr::after {
            content: '';
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, rgba(108,99,255,0.3), transparent);
        }

        /* Info card */
        .sb-info-card {
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 10px;
            font-size: 0.81rem;
            color: #c8d0e0;
            line-height: 1.6;
        }
        .sb-info-card strong { color: #a78bfa; font-weight: 600; }

        /* Goals & Values list */
        .sb-list {
            list-style: none;
            padding: 0; margin: 0;
        }
        .sb-list li {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 0;
            font-size: 0.8rem;
            color: #c8d0e0;
            border-bottom: 1px solid rgba(255,255,255,0.04);
        }
        .sb-list li:last-child { border-bottom: none; }
        .sb-list li .li-dot {
            width: 6px; height: 6px;
            border-radius: 50%;
            background: linear-gradient(135deg, #6c63ff, #4ecdc4);
            flex-shrink: 0;
        }

        /* Chat history item */
        .sb-hist-empty {
            background: rgba(255,255,255,0.025);
            border: 1px dashed rgba(108,99,255,0.2);
            border-radius: 10px;
            padding: 14px;
            text-align: center;
            font-size: 0.78rem;
            color: #8892b0;
        }

        /* Divider */
        .sb-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(108,99,255,0.25), transparent);
            margin: 16px 0;
        }
        </style>

        <div class="sb-brand">
            <div class="sb-logo">🎓</div>
            <p class="sb-college">Sri Eshwar College</p>
            <p class="sb-tagline">Department FAQ Assistant</p>
            <div class="sb-pills">
                <span class="sb-pill">RAG Powered</span>
                <span class="sb-pill">LLaMA 3.1</span>
                <span class="sb-pill">AI Bot</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── About ─────────────────────────────────────────────────────────────
        st.markdown('<div class="sb-section-hdr">ℹ️ About</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sb-info-card">
            An <strong>AI-powered FAQ assistant</strong> built exclusively for Sri Eshwar College.
            It answers queries about <strong>academics, admissions, departments,
            campus facilities, placements</strong>, and more — instantly.
        </div>
        """, unsafe_allow_html=True)

        # ── Goals ─────────────────────────────────────────────────────────────
        st.markdown('<div class="sb-section-hdr">🎯 Goals</div>', unsafe_allow_html=True)
        goals = [
            "Student Academic Support",
            "Admissions Guidance",
            "Department Information",
            "Campus Services Navigation",
            "Placement & Career Help",
            "Scholarship Assistance",
            "24/7 Accessibility",
        ]
        items_html = "".join(
            f'<li><span class="li-dot"></span>{g}</li>' for g in goals
        )
        st.markdown(
            f'<div class="sb-info-card"><ul class="sb-list">{items_html}</ul></div>',
            unsafe_allow_html=True,
        )

        # ── Our Values ────────────────────────────────────────────────────────
        st.markdown('<div class="sb-section-hdr">💎 Our Values</div>', unsafe_allow_html=True)
        values = [
            "Student-Centered",
            "Accuracy & Reliability",
            "Transparency",
            "Inclusivity",
            "Professionalism",
            "Continuous Improvement",
            "Integrity",
        ]
        items_html2 = "".join(
            f'<li><span class="li-dot"></span>{v}</li>' for v in values
        )
        st.markdown(
            f'<div class="sb-info-card"><ul class="sb-list">{items_html2}</ul></div>',
            unsafe_allow_html=True,
        )

        # ── Purpose ───────────────────────────────────────────────────────────
        st.markdown('<div class="sb-section-hdr">🚀 Purpose</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sb-info-card" style="text-align:justify;">
            Designed as a seamless, user-friendly entry point to Sri Eshwar College's
            support system, this chatbot helps students and prospective students easily
            access accurate information without confusion. Powered by a verified
            college knowledge base, it delivers trustworthy answers and connects
            users to human advisors whenever needed.
        </div>
        """, unsafe_allow_html=True)

        # ── Chat History ──────────────────────────────────────────────────────
        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sb-section-hdr">💬 Chat History</div>', unsafe_allow_html=True)

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_msgs = [
            (idx, msg)
            for idx, msg in enumerate(st.session_state.chat_history)
            if msg["role"] == "user"
        ]

        if not user_msgs:
            st.markdown(
                '<div class="sb-hist-empty">🗨️ No conversations yet.<br>Ask your first question!</div>',
                unsafe_allow_html=True,
            )
        else:
            for conv_num, (idx, msg) in enumerate(user_msgs, start=1):
                preview = msg["content"][:35] + ("…" if len(msg["content"]) > 35 else "")
                btn_label = f"💬 Q{conv_num}: {preview}"
                if st.button(btn_label, key=f"hist_{idx}"):
                    st.session_state.selected_chat = idx // 2

        # ── Clear chat ────────────────────────────────────────────────────────
        if st.session_state.chat_history:
            st.markdown('<div style="margin-top:10px;"></div>', unsafe_allow_html=True)
            if st.button("🗑️ Clear Conversation", key="clear_chat"):
                st.session_state.chat_history = []
                st.session_state.question_count = 0
                st.rerun()

        # ── PDF Export ────────────────────────────────────────────────────────
        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sb-section-hdr">📄 Export</div>', unsafe_allow_html=True)
        render_pdf_export_button(st.session_state.chat_history)

        # ── Footer ────────────────────────────────────────────────────────────
        st.markdown("""
        <div class="sb-divider"></div>
        <div style="text-align:center; font-size:0.7rem; color:#8892b0; padding-bottom:8px;">
            Made with ❤️ · Sri Eshwar College<br>
            <span style="color:#6c63ff;">FAQ Department Bot v2.0</span>
        </div>
        """, unsafe_allow_html=True)
