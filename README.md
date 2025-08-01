# 🤖 Smart Interview Bot

An AI-powered smart interview bot that conducts professional mock interviews with voice control and emotion detection, evaluates user responses, and generates a detailed feedback report in PDF format.

---

## 🔧 Features

- 🎤 **Voice Input:** Speak your answers using real-time speech-to-text.
- 📝 **Text Input:** Option to type answers manually.
- 🧠 **AI Evaluation:** NLP-based scoring and feedback system.
- 😊 **Emotion Detection:** Detects emotion from voice during response.
- 📄 **PDF Report:** Generates a downloadable report with feedback and scores.
- 🔁 **Question Rounds:** Presents 4 questions per page, rotates to the next set after evaluation.

---

## 📁 Project Structure

smart-interview-bot/
│
├── backend/ # Flask Backend
│ ├── app.py # Main Flask app
│ ├── evaluate.py # NLP evaluation logic
│ ├── emotion.py # Emotion detection from audio
│ ├── report_generator.py # PDF report creation
│ ├── questions.json # Question bank
│ ├── requirements.txt # Backend dependencies
│
├── frontend/ # React Frontend
│ ├── public/
│ │ └── index.html # HTML entry point
│ ├── src/
│ │ ├── components/
│ │ │ ├── InterviewPanel.jsx
│ │ │ ├── VoiceInput.jsx
│ │ │ ├── FeedbackBox.jsx
│ │ │ ├── EmotionDisplay.jsx
│ │ │ └── ReportDownload.jsx
│ │ ├── App.jsx # Root React component
│ │ └── index.js # ReactDOM render
│ ├── tailwind.config.js # Tailwind CSS config
│ └── package.json # Frontend dependencies


---

## ⚙️ Installation & Setup

### 🔹 Backend (Flask + Python)
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
python app.py

cd frontend
npm install
npm run start

🧪 How to Use
Launch backend and frontend servers.

App loads with a clean web interface.

First 4 questions appear → answer via text or voice.

Click "Evaluate All".

App shows:

Score

Feedback & Tips

Detected Emotion

Downloadable PDF Report

Next 4 questions will appear after clicking "Next Set".

📦 Tech Stack
Frontend: React, TailwindCSS, Web Speech API

Backend: Python, Flask, TextBlob, PyPDF2, SpeechRecognition

AI: NLP scoring, emotion detection logic (custom)

PDF: FPDF for report generation

📜 License
MIT License — Free to use and modify.

Let me know if you want the same in `.txt` or `.docx` format or want it saved to a downloadable file.

