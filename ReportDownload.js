import React from 'react';

const ReportDownload = ({ pdfLink }) => {
  if (!pdfLink) return null;

  return (
    <div className="mt-4">
      <a href={pdfLink} target="_blank" rel="noopener noreferrer" download>
        <button className="bg-purple-600 text-white p-2 rounded">📄 Download Report</button>
      </a>
    </div>
  );
};

export default ReportDownload;
