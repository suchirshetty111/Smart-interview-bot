import React from 'react';

const FeedbackBox = ({ score, feedback, tips }) => (
  <div className="bg-gray-100 p-4 rounded shadow mt-4">
    <h2 className="text-xl font-bold">Score: {score}/10</h2>
    <p className="mt-2">{feedback}</p>
    <ul className="list-disc ml-6 mt-2">
      {tips.map((tip, index) => <li key={index}>{tip}</li>)}
    </ul>
  </div>
);

export default FeedbackBox;
