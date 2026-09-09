import { useState } from "react";
import "./App.css";


function App() {
  const [idea, setIdea] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleAnalyze = async () => {
    if (!idea.trim()) {
      setError("Please enter a project idea.");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8003/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            idea: idea,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to analyze project");
      }

      const data = await response.json();

      setResult(data);

    } catch (error) {
      console.error(error);

      setError(
        "Could not connect to DevArchitect AI. Make sure all backend services are running."
      );

    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="app">

      <header className="header">
        <div>
          <h1>DevArchitect AI</h1>
          <p>Multi-Agent Software Architecture Assistant</p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI System Online
        </div>
      </header>


      <main className="container">

        <section className="hero">
          <h2>Turn Your Idea Into a Software Blueprint</h2>

          <p>
            Describe your application idea and let our AI agents analyze
            requirements, architecture, and security.
          </p>
        </section>


        <section className="input-card">

          <label>Describe Your Project Idea</label>

          <textarea
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            placeholder="Example: Build a food delivery application for Nairobi that connects customers with local restaurants and delivery riders."
          />

          <button onClick={handleAnalyze} disabled={loading}>
            {loading ? "Analyzing Project..." : "Analyze With AI"}
          </button>

          {error && (
            <p className="error">{error}</p>
          )}

        </section>


        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>DevArchitect AI agents are analyzing your project...</p>
          </div>
        )}


        {result && (
          <section className="results">

            <h2>AI Analysis Results</h2>

            <div className="result-card">

              <h3>DevArchitect Multi-Agent Analysis</h3>

              <pre>
                {JSON.stringify(result, null, 2)}
              </pre>

            </div>

          </section>
        )}

      </main>

    </div>
  );
}


export default App;