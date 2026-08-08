import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// ====================
// Candidate
// ====================

export interface Education {
  degree: string;
  graduation_year: number;
}

export interface Candidate {
  id: string;
  name: string;
  email: string;
  role: string;
  experience_level: string;
  skills: string[];
  education: Education;
}

// ====================
// Curriculum
// ====================

export interface Module {
  id: string;
  name: string;
  day: number;
  description: string;
  topics: string[];
}

export interface Curriculum {
  title: string;
  version: string;
  description: string;
  modules: Module[];
}

// ====================
// Interview
// ====================

export interface InterviewQuestion {
  id: string;
  question: string;
  topic: string;
  difficulty: string;
}

export interface InterviewSession {
  candidate_id: string;
  current_question: InterviewQuestion | null;
  question_number: number;
  total_questions: number;
}

export interface AnswerSubmission {
  candidate_id: string;
  question_id: string;
  answer: string;
}

export interface AnswerResponse {
  candidate_id: string;
  question_id: string;
  answer: string;
  next_question: InterviewQuestion | null;
  completed: boolean;
}

// ====================
// Interview Memory
// ====================

export interface InterviewAnswer {
  question_id: string;
  answer: string;
}

// ====================
// Candidate API
// ====================

export const fetchCandidate = async (): Promise<Candidate> => {
  const response = await apiClient.get<Candidate>("/api/candidate");
  return response.data;
};

// ====================
// Curriculum API
// ====================

export const fetchCurriculum = async (): Promise<Curriculum> => {
  const response = await apiClient.get<Curriculum>("/api/curriculum");
  return response.data;
};

// ====================
// Interview API
// ====================

export const startInterview = async (
  candidateId: string
): Promise<InterviewSession> => {
  const response = await apiClient.post<InterviewSession>(
    "/api/interview/start",
    null,
    {
      params: {
        candidate_id: candidateId,
      },
    }
  );

  return response.data;
};

export const getInterviewQuestion = async (
  questionNumber: number
): Promise<InterviewQuestion> => {
  const response = await apiClient.get<InterviewQuestion>(
    `/api/interview/question/${questionNumber}`
  );

  return response.data;
};

export const submitAnswer = async (
  submission: AnswerSubmission
): Promise<AnswerResponse> => {
  const response = await apiClient.post<AnswerResponse>(
    "/api/interview/answer",
    submission
  );

  return response.data;
};

// ====================
// Interview Memory API
// ====================

export const getInterviewMemory = async (
  candidateId: string
): Promise<InterviewAnswer[]> => {
  const response = await apiClient.get<InterviewAnswer[]>(
    `/api/interview/memory/${candidateId}`
  );

  return response.data;
};

// ====================
// Feedback API
// ====================

export interface FeedbackResponse {
  candidate_id: string;
  overall_score: number;
  technical_score: number;
  communication_score: number;
  strengths: string[];
  weaknesses: string[];
  recommendations: string[];
}

export const generateFeedback = async (
  candidateId: string
): Promise<FeedbackResponse> => {
  const response = await apiClient.post<FeedbackResponse>(
    "/api/feedback/generate",
    {
      candidate_id: candidateId,
    }
  );

  return response.data;
};