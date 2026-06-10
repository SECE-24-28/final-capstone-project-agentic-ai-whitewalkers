import os
import streamlit as st
from fpdf import FPDF
from datetime import datetime

from utils import remove_emojis


def render_pdf_export_button(chat_history):
    """Render the 'Export Chat to PDF' button and handle PDF generation and download."""
    if st.button("Export Chat to PDF"):
        if len(chat_history) > 0:
            try:
                # Create PDF
                pdf = FPDF()
                pdf.add_page()

                # Use Arial font
                pdf.set_font('Arial', '', 10)

                # PDF Header
                pdf.set_font('Arial', 'B', 16)
                pdf.cell(0, 10, "College Name Chatbot - Conversation History", ln=True, align='C')
                pdf.set_font('Arial', '', 12)
                pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
                pdf.ln(10)

                # Add conversation messages
                pdf.set_font('Arial', '', 10)
                for message in chat_history:
                    # Role header
                    pdf.set_font('Arial', 'B', 10)
                    pdf.cell(0, 10, message["role"].capitalize(), ln=True)
                    # Message content
                    pdf.set_font('Arial', '', 10)
                    pdf.multi_cell(0, 10, remove_emojis(message["content"]))
                    pdf.ln(5)

                # Save PDF to a temporary file
                filename = f"mental_health_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                pdf.output(filename)

                # Create download button
                with open(filename, "rb") as f:
                    st.download_button(
                        label="Download PDF",
                        data=f,
                        file_name=filename,
                        mime="application/pdf"
                    )

                # Clean up the temporary file
                os.remove(filename)

            except Exception as e:
                st.error(f"Error generating PDF: {str(e)}")
        else:
            st.warning("No chat history to export!")
