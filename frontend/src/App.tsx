import { useState } from "react";

import Landing from "./pages/Landing";
import Interview from "./pages/Interview";
import Dashboard from "./pages/Dashboard";

import type { InterviewSession } from "./services/api";

function App() {
  const [interviewSession, setInterviewSession] =
    useState<InterviewSession | null>(null);

  const [interviewCompleted, setInterviewCompleted] =
    useState(false);

  const path = window.location.pathname;

  // Final feedback dashboard
  if (path === "/dashboard" || interviewCompleted) {
    return <Dashboard candidateId="candidate_001" />;
  }

  // Active interview
  if (
    interviewSession &&
    interviewSession.current_question
  ) {
    return (
      <Interview
        candidateId={interviewSession.candidate_id}
        firstQuestion={interviewSession.current_question}
        totalQuestions={interviewSession.total_questions}
        onComplete={() => setInterviewCompleted(true)}
      />
    );
  }

  // Landing page
  return (
    <Landing
      onInterviewStarted={setInterviewSession}
    />
  );
}

export default App;
