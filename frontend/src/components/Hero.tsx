import { useState } from "react";
import { startInterview } from "../services/api";
import type { InterviewSession } from "../services/api";

interface HeroProps {
  onInterviewStarted: (session: InterviewSession) => void;
}

export default function Hero({ onInterviewStarted }: HeroProps) {
  const [loading, setLoading] = useState(false);

  const handleStartInterview = async () => {
    try {
      setLoading(true);

      const session = await startInterview("candidate_001");

      console.log("Interview started:", session);

      if (!session.current_question) {
        alert("Interview started, but no question was received.");
        return;
      }

      onInterviewStarted(session);
    } catch (error) {
      console.error("Failed to start interview:", error);

      alert(
        "Unable to start the interview. Please make sure the FastAPI backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="py-20">
      <div className="mx-auto max-w-6xl px-6 text-center">

        <div className="mb-6 inline-block rounded-full border bg-gray-50 px-4 py-2 text-sm text-gray-600">
          🤖 AI-Powered Interview Platform
        </div>

        <h1 className="max-w-4xl mx-auto text-4xl font-bold tracking-tight text-gray-900 md:text-6xl">
          Practice Interviews with
          <span className="block text-gray-600">
            Your AI Interview Agent
          </span>
        </h1>

        <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-gray-600">
          Experience realistic AI-powered interviews that adapt to your
          skills, analyze your answers, and provide personalized feedback
          to help you improve.
        </p>

        <div className="mt-8 flex flex-col justify-center gap-4 sm:flex-row">
          <button
            onClick={handleStartInterview}
            disabled={loading}
            className="rounded-md bg-black px-6 py-3 font-medium text-white hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Starting Interview..." : "Start Interview →"}
          </button>

          {/* <button
            className="rounded-md border px-6 py-3 font-medium text-gray-700 hover:bg-gray-50"
          >
            Learn More
          </button> */}
        </div>

      </div>
    </section>
  );
}