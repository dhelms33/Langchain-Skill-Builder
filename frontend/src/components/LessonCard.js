import React from "react";

function LessonCard({ skill }) {
  return (
    <div className="lesson-card">
      <h2>Learn {skill}</h2>
      <p>This is a sample lesson for {skill}.</p>
    </div>
  );
}

export default LessonCard;
