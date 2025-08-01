import React from 'react';

const EmotionDisplay = ({ emotion }) => (
  <div className="mt-4 text-lg">
    <strong>Detected Emotion:</strong> <span className="text-blue-600">{emotion}</span>
  </div>
);

export default EmotionDisplay;
