import React, { useState } from 'react';
import VoiceInput from './VoiceInput';
import FeedbackBox from './FeedbackBox';
import EmotionDisplay from './EmotionDisplay';
import ReportDownload from './ReportDownload';

const questions = [
  "Tell me about yourself.",
  "Why should we hire you?",
  "What are your strengths and weaknesses?",
  "Describe a challenge you faced and how you overcame it."
];

function InterviewPanel() {
  const [answers, setAnswers] = useState(["", "", "", ""]);
  const [results, setResults] = useState(null);
  const [pdfLink, setPdfLink] = useState(null);

  const handleChange = (index, value) => {
    const updated = [...answers];
    updated[index] = value;
    setAnswers(updated);
  };

  const handleEvaluateAll = async () => {
    const res = await fetch("http://localhost:5000/api/evaluate-multiple", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers })
    });
    const data = await res.json();
    setResults(data.results);
    setPdfLink(data.pdf);
  };

  return (
    <div className="mt-6 bg-white p-6 rounded-lg shadow-md max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Smart Interview Bot</h2>
      
      {questions.map((q, index) => (
        <div key={index} className="mb-6">
          <p className="font-medium text-gray-700 mb-2">{q}</p>
          <textarea
            value={answers[index]}
            onChange={(e) => handleChange(index, e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md"
            rows={3}
            placeholder="Type your answer or use voice"
          />
          <VoiceInput setAnswer={(val) => handleChange(index, val)} />
        </div>
      ))}

      <button
        onClick={handleEvaluateAll}
        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded"
      >
        Evaluate All
      </button>

      {results && (
        <div className="mt-8 space-y-6">
          {results.map((res, i) => (
            <div key={i} className="p-4 border rounded bg-gray-50">
              <h4 className="font-semibold text-gray-800 mb-2">{questions[i]}</h4>
              <FeedbackBox feedback={res.feedback} tips={res.tips} score={res.score} />
              <EmotionDisplay emotion={res.emotion} />
            </div>
          ))}
          <ReportDownload pdfLink={pdfLink} />
        </div>
      )}
    </div>
  );
}

export default InterviewPanel;
