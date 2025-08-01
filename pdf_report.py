from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf_report(answer, score, feedback, tips, emotion):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Interview Answer Evaluation", ln=True, align="C")
    pdf.set_font("Arial", "", 12)

    pdf.ln(10)
    pdf.multi_cell(0, 8, f"Answer: {answer}")
    pdf.multi_cell(0, 8, f"Score: {score} / 10")
    pdf.multi_cell(0, 8, f"Feedback: {feedback}")
    pdf.multi_cell(0, 8, f"Emotion Detected: {emotion}")
    tips_text = "\n".join([f"- {tip}" for tip in tips])
    pdf.multi_cell(0, 8, f"Tips for Improvement:\n{tips_text}")

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    path = os.path.join("services", "reports", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pdf.output(path)
    return filename

def generate_pdf_report_multiple(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Interview Summary Report", ln=True, align="C")
    pdf.set_font("Arial", "", 12)

    for idx, r in enumerate(results):
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, f"Question {idx+1}:", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, f"Answer: {r['answer']}")
        pdf.multi_cell(0, 8, f"Score: {r['score']} / 10")
        pdf.multi_cell(0, 8, f"Emotion: {r['emotion']}")
        pdf.multi_cell(0, 8, f"Feedback: {r['feedback']}")
        tips_text = "\n".join([f"- {tip}" for tip in r['tips']])
        pdf.multi_cell(0, 8, f"Tips:\n{tips_text}")

    filename = f"interview_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    path = os.path.join("services", "reports", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pdf.output(path)
    return filename
