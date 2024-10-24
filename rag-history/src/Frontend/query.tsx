import React, { useState, FormEvent, useRef, useEffect} from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser as userIcon, faRobot as botIcon } from "@fortawesome/free-solid-svg-icons";
import "../Styling/query.css";

interface QueryProps {
  userId: string;
}

const Query: React.FC<QueryProps> = ({ userId }) => {
  const [question, setQuestion] = useState<string>("");
  const [responses, setResponses] = useState<{ text: string; isUser: boolean }[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  const responseEndRef = useRef<HTMLDivElement>(null);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setResponses((prev) => [...prev, { text: question, isUser: true }]);
    setQuestion("");
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:5000/query", 
        { question, user_id: userId },
        { 
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      setResponses((prev) => [...prev, { text: res.data.response, isUser: false }]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setResponses((prev) => [
        ...prev,
        { text: "Error fetching response", isUser: false },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey && !loading) {
      e.preventDefault();
      handleSubmit(e as unknown as FormEvent<HTMLFormElement>);
    }
  };

  useEffect(() => {
    if (responseEndRef.current) {
      responseEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [responses]);

  return (
    <div className="chat-container">
      <div className="response-container">
        {responses.map((response, index) => (
          <div
            key={index}
            className={`response-message ${response.isUser ? "user" : "bot"}`}
          >
            {response.isUser ? (
              <div style={{ display: "flex", alignItems: "center" }}>
                <p className="response-text">{response.text}</p>
                <FontAwesomeIcon icon={userIcon} className="user-icon" />
              </div>
            ) : (
              <div style={{ display: "flex", alignItems: "center" }}>
                <FontAwesomeIcon icon={botIcon} className="bot-icon" />
                <p className="response-text">{response.text}</p>
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="response-message bot">
            <div className="spinner"></div>
          </div>
        )}
        <div ref={responseEndRef} />
      </div>
      <form onSubmit={handleSubmit} className="input-form">
        <textarea
          className="input-box"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask your question"
          required
          onKeyDown={handleKeyDown}
          disabled={loading}
        />
      </form>
    </div>
  );
};

export default Query;