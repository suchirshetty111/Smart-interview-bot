import React from 'react';

const VoiceInput = ({ setAnswer }) => {
  const startListening = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setAnswer(transcript);
    };
    recognition.start();
  };

  return (
    <button onClick={startListening} className="mt-2 bg-green-500 text-white p-2 rounded">
      🎤 Speak Answer
    </button>
  );
};

export default VoiceInput;
