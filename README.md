# AI Interview Agent

> An adaptive AI-powered technical interview system built for the **ABTalks AI Cohort Hackathon 2026**.

AI Interview Agent is a full-stack technical interview platform that simulates an interviewer, asks curriculum-based questions, remembers the candidate's answers, generates contextual follow-up questions, adapts interview difficulty, and produces a structured performance report.

The project is designed with a modular architecture so that the AI provider can be replaced or upgraded without rewriting the core interview system.

---

## 🚀 Live Demo

**Frontend:**  
https://ai-interview-agent-ecru-five.vercel.app/

**Backend API:**  
https://ai-interview-agent-p18a.onrender.com/

**Backend Health Check:**  
https://ai-interview-agent-p18a.onrender.com/health

**API Documentation:**  
https://ai-interview-agent-p18a.onrender.com/docs

---

## 📌 Project Overview

Traditional interview applications often follow a fixed list of questions.

AI Interview Agent takes a different approach.

The system maintains interview context and uses the candidate's previous responses to create a more personalized interview experience.

### Interview flow

```text
Candidate Profile
       ↓
Curriculum
       ↓
Start Interview
       ↓
Generate Question
       ↓
Candidate Answer
       ↓
Analyze Performance
       ↓
Adjust Difficulty
       ↓
Generate Next Question
       ↓
Optional Follow-up
       ↓
Interview Completion
       ↓
AI Feedback
       ↓
Performance Dashboard