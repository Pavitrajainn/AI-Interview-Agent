import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features-temp";

export default function Landing() {
  return (
    <div className="min-h-screen bg-white">
      <Navbar />
      <Hero />
      <Features />
    </div>
  );
}