import { useEffect, useState } from "react";
import {
  generateFeedback,
  type FeedbackResponse,
} from "../services/api";

interface DashboardProps {
  candidateId: string;
}

export default function Dashboard({
  candidateId,
}: DashboardProps) {
  const [feedback, setFeedback] =
    useState<FeedbackResponse | null>(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadFeedback = async () => {
      try {
        setLoading(true);
        setError("");

        const result = await generateFeedback(candidateId);

        setFeedback(result);
      } catch (err) {
        console.error("Failed to load feedback:", err);
        setError(
          "Unable to load interview feedback. Please try again."
        );
      } finally {
        setLoading(false);
      }
    };

    loadFeedback();
  }, [candidateId]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gray-50 px-6 py-12">
        <div className="mx-auto max-w-5xl text-center">
          <p className="text-gray-600">
            Generating your interview feedback...
          </p>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="min-h-screen bg-gray-50 px-6 py-12">
        <div className="mx-auto max-w-5xl text-center">
          <p className="text-red-600">{error}</p>
        </div>
      </main>
    );
  }

  if (!feedback) {
    return null;
  }

  return (
    <main className="min-h-screen bg-gray-50 px-6 py-12">
      <div className="mx-auto max-w-5xl">

        <div className="mb-10">
          <h1 className="text-3xl font-bold">
            Interview Results
          </h1>

          <p className="mt-2 text-gray-600">
            Here is your AI interview performance report.
          </p>
        </div>

        {/* Scores */}
        <div className="grid gap-6 md:grid-cols-3">

          <div className="rounded-xl bg-white p-6 shadow">
            <p className="text-sm text-gray-500">
              Overall Score
            </p>

            <p className="mt-2 text-4xl font-bold">
              {feedback.overall_score}
            </p>
          </div>

          <div className="rounded-xl bg-white p-6 shadow">
            <p className="text-sm text-gray-500">
              Technical Score
            </p>

            <p className="mt-2 text-4xl font-bold">
              {feedback.technical_score}
            </p>
          </div>

          <div className="rounded-xl bg-white p-6 shadow">
            <p className="text-sm text-gray-500">
              Communication Score
            </p>

            <p className="mt-2 text-4xl font-bold">
              {feedback.communication_score}
            </p>
          </div>

        </div>

        {/* Strengths */}
        <section className="mt-8 rounded-xl bg-white p-6 shadow">
          <h2 className="text-xl font-semibold">
            Strengths
          </h2>

          <ul className="mt-4 list-disc space-y-2 pl-5 text-gray-700">
            {feedback.strengths.map((strength, index) => (
              <li key={index}>{strength}</li>
            ))}
          </ul>
        </section>

        {/* Weaknesses */}
        <section className="mt-6 rounded-xl bg-white p-6 shadow">
          <h2 className="text-xl font-semibold">
            Areas to Improve
          </h2>

          <ul className="mt-4 list-disc space-y-2 pl-5 text-gray-700">
            {feedback.weaknesses.map((weakness, index) => (
              <li key={index}>{weakness}</li>
            ))}
          </ul>
        </section>

        {/* Recommendations */}
        <section className="mt-6 rounded-xl bg-white p-6 shadow">
          <h2 className="text-xl font-semibold">
            Learning Recommendations
          </h2>

          <ul className="mt-4 list-disc space-y-2 pl-5 text-gray-700">
            {feedback.recommendations.map(
              (recommendation, index) => (
                <li key={index}>{recommendation}</li>
              )
            )}
          </ul>
        </section>

      </div>
    </main>
  );
}