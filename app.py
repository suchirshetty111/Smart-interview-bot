from flask import Flask, request, jsonify, send_file
from services.evaluator import evaluate_answer
from services.voice_to_text import speech_to_text
from services.emotion_detector import detect_emotion
from services.pdf_report import generate_pdf_report, generate_pdf_report_multiple
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def root():
    return "✅ Smart Interview Bot backend is running!"

@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    answer = data.get("answer", "")
    score, feedback, tips = evaluate_answer(answer)
    emotion = detect_emotion(answer)
    filename = generate_pdf_report(answer, score, feedback, tips, emotion)
    return jsonify({
        "score": score,
        "feedback": feedback,
        "tips": tips,
        "emotion": emotion,
        "pdf": f"http://localhost:5000/api/report/{filename}"
    })

@app.route("/api/evaluate-multiple", methods=["POST"])
def evaluate_multiple():
    data = request.get_json()
    answers = data.get("answers", [])

    results = []
    for ans in answers:
        score, feedback, tips = evaluate_answer(ans)
        emotion = detect_emotion(ans)
        results.append({
            "answer": ans,
            "score": score,
            "feedback": feedback,
            "tips": tips,
            "emotion": emotion
        })

    filename = generate_pdf_report_multiple(results)
    return jsonify({
        "results": results,
        "pdf": f"http://localhost:5000/api/report/{filename}"
    })

@app.route("/api/speech", methods=["POST"])
def speech():
    audio_file = request.files['file']
    transcript = speech_to_text(audio_file)
    return jsonify({"text": transcript})

@app.route("/api/report/<filename>", methods=["GET"])
def download_report(filename):
    return send_file(f"services/reports/{filename}", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
