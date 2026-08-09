import { useState } from "react";

import {
  submitAnswer,
  generateFollowUp,
} from "../services/api";

import type { InterviewQuestion } from "../services/api";

interface InterviewProps {
  candidateId: string;
  firstQuestion: InterviewQuestion;
  totalQuestions: number;
  onComplete: () => void;
}

export default function Interview({
  candidateId,
  firstQuestion,
  totalQuestions,
  onComplete,
}: InterviewProps) {
  const [currentQuestion, setCurrentQuestion] =
    useState(firstQuestion);

  const [questionNumber, setQuestionNumber] =
    useState(1);

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  const [followUp, setFollowUp] = useState("");

  const [followUpLoading, setFollowUpLoading] =
    useState(false);

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

      setFollowUp("");

      if (response.completed) {
        onComplete();
        return;
      }

      if (response.next_question) {
        setCurrentQuestion(response.next_question);

        setQuestionNumber(
          (previous) => previous + 1
        );

        setAnswer("");
      }
    } catch (error) {
      console.error(
        "Failed to submit answer:",
        error
      );

      alert(
        "Unable to submit answer. Check if backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateFollowUp = async () => {
    if (!answer.trim()) {
      alert(
        "Please enter your answer before requesting a follow-up."
      );
      return;
    }

    try {
      setFollowUpLoading(true);

      const response = await generateFollowUp(
        candidateId,
        currentQuestion.id,
        answer.trim()
      );

      setFollowUp(
        response.follow_up_question
      );
    } catch (error) {
      console.error(
        "Failed to generate follow-up:",
        error
      );

      alert(
        "Unable to generate follow-up question."
      );
    } finally {
      setFollowUpLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 px-6 py-10">
      <div className="mx-auto max-w-4xl">

        {/* Header */}

        <div className="mb-8 flex items-center justify-between">
          <h1 className="text-2xl font-bold">
            AI Technical Interview
          </h1>

          <span className="rounded-full bg-gray-200 px-4 py-2 text-sm">
            Question {questionNumber} /{" "}
            {totalQuestions}
          </span>
        </div>

        {/* Question Card */}

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

          {/* Answer */}

          <textarea
            value={answer}
            onChange={(event) =>
              setAnswer(event.target.value)
            }
            placeholder="Type your answer here..."
            rows={8}
            disabled={loading}
            className="mt-6 w-full rounded-lg border p-4 outline-none"
          />

          {/* Actions */}

          <div className="mt-6 flex flex-wrap gap-3">

            <button
              onClick={handleSubmitAnswer}
              disabled={
                loading ||
                followUpLoading ||
                !answer.trim()
              }
              className="rounded-md bg-black px-6 py-3 text-white disabled:opacity-50"
            >
              {loading
                ? "Submitting..."
                : "Submit Answer → "}
            </button>

            <button
              onClick={handleGenerateFollowUp}
              disabled={
                loading ||
                followUpLoading ||
                !answer.trim()
              }
              className="rounded-md border border-gray-300 bg-white px-6 py-3 text-gray-800 disabled:opacity-50"
            >
              {followUpLoading
                ? "Generating..."
                : "Ask Follow-up"}
            </button>

          </div>

          {/* Follow-up */}

          {followUp && (
            <div className="mt-6 rounded-lg border border-blue-200 bg-blue-50 p-5">

              <p className="text-sm font-medium text-blue-600">
                AI Follow-up Question
              </p>

              <p className="mt-2 text-lg font-medium text-gray-900">
                {followUp}
              </p>

            </div>
          )}

        </div>
      </div>
    </main>
  );
}

