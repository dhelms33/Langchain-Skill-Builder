import React from "react";
import LessonCard from "./components/LessonCard";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Skill Builder</h1>
        <LessonCard skill="Python Programming" />
      </header>
    </div>
  );
}

export default App;
