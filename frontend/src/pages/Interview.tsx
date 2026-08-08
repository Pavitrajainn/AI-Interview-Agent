import { useState } from "react";
import { submitAnswer } from "../services/api";
import type { InterviewQuestion } from "../services/api";

interface InterviewProps {
  candidateId: string;
  firstQuestion: InterviewQuestion;
  totalQuestions: number;
}

export default function Interview({
  candidateId,
  firstQuestion,
  totalQuestions,
}: InterviewProps) {
  const [currentQuestion, setCurrentQuestion] =
    useState<InterviewQuestion>(firstQuestion);

  const [questionNumber, setQuestionNumber] = useState(1);
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [completed, setCompleted] = useState(false);

  const handleSubmitAnswer = async () => {
    if (!answer.trim()) {
      alert("Please enter your answer.");
      return;
    }

    try {
      setLoading(true);

      const response = await submitAnswer({
        candidate_id: candidateId,
        question_id: currentQuestion.id,
        answer: answer.trim(),
      });

      if (response.completed) {
        setCompleted(true);
        return;
      }

      if (response.next_question) {
        setCurrentQuestion(response.next_question);
        setQuestionNumber((previous) => previous + 1);
        setAnswer("");
      }
    } catch (error) {
      console.error("Failed to submit answer:", error);
      alert("Unable to submit answer. Check if backend is running.");
    } finally {
      setLoading(false);
    }
  };

  if (completed) {
    return (
      <main className="min-h-screen bg-gray-50 p-8">
        <div className="mx-auto max-w-3xl rounded-xl bg-white p-8 text-center shadow">
          <h1 className="text-3xl font-bold">
            Interview Completed!
          </h1>

          <p className="mt-4 text-gray-600">
            You completed all {totalQuestions} questions.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-3xl">

        <div className="mb-8 flex items-center justify-between">
          <h1 className="text-2xl font-bold">
            AI Technical Interview
          </h1>

          <span className="rounded-full bg-gray-200 px-4 py-2 text-sm">
            Question {questionNumber} / {totalQuestions}
          </span>
        </div>

        <div className="rounded-xl bg-white p-8 shadow">

          <div className="mb-4 flex justify-between">
            <span className="text-sm text-gray-500">
              {currentQuestion.topic}
            </span>

            <span className="text-sm capitalize text-gray-500">
              {currentQuestion.difficulty}
            </span>
          </div>

          <h2 className="text-2xl font-semibold">
            {currentQuestion.question}
          </h2>

          <textarea
            value={answer}
            onChange={(event) => setAnswer(event.target.value)}
            placeholder="Type your answer here..."
            rows={8}
            disabled={loading}
            className="mt-6 w-full rounded-lg border p-4 outline-none"
          />

          <button
            onClick={handleSubmitAnswer}
            disabled={loading || !answer.trim()}
            className="mt-6 rounded-md bg-black px-6 py-3 text-white disabled:opacity-50"
          >
            {loading ? "Submitting..." : "Submit Answer →"}
          </button>

        </div>
      </div>
    </main>
  );
}

