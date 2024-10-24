import React, { useState, useCallback } from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faCircleUser, faSpinner, faTrash, faRotateRight } from "@fortawesome/free-solid-svg-icons";
import Query from "./query";
import { getUserId, resetUserId } from './userUtils';
import "../Styling/App.css";

interface ChatMessage {
  id: string;
  timestamp: string;
  question: string;
  response: string;
  user_id: string;
}

const App: React.FC = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState<boolean>(false);
  const [chatHistory, setChatHistory] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [deletingId, setDeletingId] = useState<string | null>(null);
  const [userId, setUserId] = useState<string>(getUserId());

  const handleResetUserId = async () => {
    const newUserId = resetUserId();
    setUserId(newUserId);
    setChatHistory([]); // Clear chat history for new user
    // Optionally show a confirmation message
    alert(`User ID has been reset. New ID: ${newUserId}`);
  };

  const toggleDropdown = async (): Promise<void> => {
    setIsDropdownOpen(!isDropdownOpen);
    if (!isDropdownOpen) {
      await fetchChatHistory();
    }
  };

  const fetchChatHistory = useCallback(async () => {
    setLoading(true);
    try {
      const res = await axios.get(`http://127.0.0.1:5000/chat_history`, {
        params: { user_id: userId },
        headers: {
          'Content-Type': 'application/json'
        }
      });
      const history: ChatMessage[] = res.data;
      setChatHistory(history);
    } catch (error) { 
      console.error("Error fetching chat history:", error);
    }
    finally {
      setLoading(false);
    }
  }, [userId]);
  
  const deleteChat = async (chatId: string) => {
    setDeletingId(chatId);
    try {
        const response = await axios.delete(`http://127.0.0.1:5000/chat_history/${chatId}`, {
            params: { user_id: userId },
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (response.status === 200) {
            setChatHistory(prevHistory => 
                prevHistory.filter(chat => chat.id !== chatId)
            );
            console.log("Successfully deleted chat message");
        } else {
            console.error("Failed to delete chat message");
        }
    } catch (error) {
        console.error("Error deleting chat:", error);
    } finally {
        setDeletingId(null);
    }
};

  const dropdownStyle = {
    position: 'fixed' as const,
    top: '100px',
    left: isDropdownOpen ? '0' : '-320px',
    width: '320px',
    height: 'calc(100vh - 100px)',
    backgroundColor: '#282c34',
    borderRight: '1px solid #3a3a3a',
    overflowY: 'auto' as const,
    zIndex: 1000,
    transition: 'left 1s ease, opacity 1s ease',
  };

  return (
    <div className="App">
      <div className="App-header">
        <FontAwesomeIcon 
          icon={faBars} 
          className="dropdown-icon"
          onClick={toggleDropdown}
          style={{
            transform: isDropdownOpen ? 'rotate(90deg)' : 'rotate(0)',
            transition: 'transform 1s ease',
            cursor: 'pointer',
          }}
        />
        <h1>History Agent</h1>
        <div>
          <span style={{ 
            color: '#b4b4b4', 
            fontSize: '1.2rem' 
          }}>
            ID: {userId}
          </span>
          <button
            onClick={handleResetUserId}
            style={{
              background: 'none',
              border: 'none',
              color: '#b4b4b4',
              cursor: 'pointer',
              padding: '8px',
              display: 'flex',
              alignItems: 'center',
              gap: '5px',
              marginTop: '10px',
              borderRadius: '4px',
              transition: 'all 0.3s ease',
            }}
            onMouseOver={(e) => e.currentTarget.style.backgroundColor = '#3a3a3a'}
            onMouseOut={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
          >
            <FontAwesomeIcon icon={faRotateRight} />
            <span style={{ fontSize: '0.8rem' }}>Reset ID</span>
          </button>
        </div>
      </div>
      <div style={dropdownStyle}>
        {loading ? (
          <div style={{ 
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100px',
            color: '#b4b4b4',
          }}>
            <FontAwesomeIcon icon={faSpinner} spin size="2x" />
          </div>
        ) : (
          <>
            <h2 style={{ 
              color: '#fff', 
              marginBottom: '20px',
              fontSize: '1.2rem',
              marginLeft: '100px',
            }}>
              Chat History
            </h2>
            {chatHistory.length > 0 ? (
              chatHistory.map((chat) => (
                <div 
                  key={`${chat.id}-${chat.timestamp}`}
                  style={{
                    backgroundColor: '#323842',
                    margin: '10px',
                    padding: '15px',
                    borderRadius: '5px',
                    position: 'relative',
                    opacity: isDropdownOpen ? 1 : 0,
                    transform: `translateX(${isDropdownOpen ? '0' : '20px'})`,
                    transition: 'all 0.3s ease',
                  }}
                >
                  <div style={{ color: '#fff', wordBreak: 'break-word' }}>
                    <div>{chat.question}</div>
                    <div>{chat.response}</div>
                  </div>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      if (chat.id) deleteChat(chat.id);
                    }}
                    style={{
                      position: 'absolute',
                      top: '4px',
                      right: '2px',
                      background: 'none',
                      border: 'none',
                      color: '#ffffff',
                      cursor: 'pointer',
                      opacity: 1,
                      transition: 'opacity 0.3s ease',
                      padding: '4px',
                    }}
                    onMouseOver={(e) => (e.currentTarget.style.opacity = '1')}
                    onMouseOut={(e) => (e.currentTarget.style.opacity = '0.7')}
                  >
                    {deletingId === chat.id ? (
                      <FontAwesomeIcon icon={faSpinner} spin />
                    ) : (
                      <FontAwesomeIcon icon={faTrash} />
                    )}
                  </button>
                </div>
              ))
            ) : (
              <div style={{
                textAlign: 'center',
                color: '#b4b4b4',
                padding: '20px',
              }}>
                No chat history available
              </div>
            )}
          </>
        )}
      </div>

      <div className="chat-container">
        <Query userId={userId} />
      </div>
    </div>
  );
};

export default App;