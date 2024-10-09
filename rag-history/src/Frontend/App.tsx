import React from "react";
import Query from "./query";
import "../Styling/App.css";

const App: React.FC = () => {
  return (
    <div className="App">
      <div className="App-header">
        <h1>History Agent</h1>
      </div>
      <div className="chat-container">
        <Query />
      </div>
    </div>
  );
};

export default App;
