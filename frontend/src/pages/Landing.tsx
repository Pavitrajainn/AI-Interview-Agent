import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features-temp";
import type { InterviewSession } from "../services/api";

interface LandingProps {
  onInterviewStarted: (session: InterviewSession) => void;
}

export default function Landing({
  onInterviewStarted,
}: LandingProps) {
  return (
    <div className="min-h-screen bg-white">
      <Navbar />

      <Hero onInterviewStarted={onInterviewStarted} />

      <Features />
    </div>
  );
}