# PROMPTS.md

## Prompt 1

### Goal

Understand the hackathon requirements.

### Context

The project is an AI Interview Agent for the ABTalks AI Cohort Hackathon.

### Prompt

You are a Senior AI Solutions Architect.

Analyze the hackathon problem statement and create a complete Software Requirement Specification (SRS) including functional requirements, architecture, modules, API requirements, technology stack, and development roadmap.

### Expected Output

A detailed SRS document that will act as the blueprint for the project.

### Engineering Reason

Every production-grade software project should begin with proper requirement analysis before implementation.

## Prompt 2

### Goal
Set up a production-ready backend for the AI Interview Agent.

### Context
The project requires REST APIs for starting interviews, processing answers, and generating feedback.

### Prompt
You are a Senior Backend Engineer.

Design a production-ready FastAPI backend structure for an AI Interview Agent using modular architecture. Include API routes, services, models, utilities, and configuration files.

### Expected Output
A clean backend folder structure and FastAPI application entry point.

### Engineering Reason
A modular backend makes the project scalable and easier to maintain.

## Prompt 3

### Goal

Setup the frontend application for the AI Interview Agent.

### Context

The project requires a modern frontend interface for candidate interaction, interview flow, and feedback visualization.

### Prompt

You are a Senior Frontend Engineer.

Create a production-ready React frontend using Vite, TypeScript, and a scalable folder structure. Configure the project for future integration with FastAPI backend APIs.

### Expected Output

A working React + TypeScript + Vite frontend application.

### Engineering Reason

A modern frontend architecture improves maintainability, scalability, and developer experience.


## Prompt 4

### Goal

Configure Tailwind CSS for frontend styling.

### Context

The AI Interview Agent requires a responsive and professional user interface.

### Prompt

You are a Senior Frontend Engineer.

Setup Tailwind CSS in a Vite React TypeScript project and configure it for reusable component-based UI development.

### Expected Output

A working Tailwind CSS configuration with utility-based styling support.

### Engineering Reason

Tailwind CSS enables rapid development of consistent, responsive, and maintainable user interfaces.

## Prompt 5

### Goal

Setup shadcn/ui component library for the AI Interview Agent frontend.

### Context

The project requires reusable, accessible, and production-ready UI components for building the interview interface.

### Prompt

You are a Senior Frontend Engineer.

Configure shadcn/ui in a React + TypeScript + Vite project with Tailwind CSS. Add reusable UI components required for future pages and interactions.

### Expected Output

A configured shadcn/ui system with reusable components like Button, Card, and Input.

### Engineering Reason

Reusable component libraries improve UI consistency, accessibility, and development speed.

## Prompt 6 — Landing Page Design

### Goal

Create a professional and responsive landing page for the AI Interview Agent.

### Completed

- Created `Navbar.tsx`
- Created `Hero.tsx`
- Created `Features.tsx`
- Created `Landing.tsx`
- Integrated landing page with `App.tsx`
- Added responsive Tailwind styling
- Added AI Interview Agent branding
- Added feature cards
- Added Start Interview CTA

## Prompt 7 — Candidate Profile Loader

### Goal

Create a structured candidate profile system that loads candidate information from JSON, validates it using Pydantic, and exposes it through a FastAPI endpoint.

### Requirements

- Create a structured candidate JSON file.
- Create a Pydantic Candidate model.
- Create an Education model for candidate education details.
- Create a Candidate Service to load candidate data.
- Create a FastAPI Candidate API route.
- Register the Candidate API router in the main FastAPI application.
- Validate candidate data using Pydantic.
- Expose candidate information through a REST API.

### Implementation

Created:

```text
backend/
├── data/
│   └── candidate.json
│
└── app/
    ├── api/
    │   └── candidate.py
    │
    ├── models/
    │   └── candidate.py
    │
    └── services/
        └── candidate_service.py
```

### API Endpoint

```text
GET /api/candidate
```

---

## Prompt 8 — Curriculum JSON Loader

### Goal

Create a structured curriculum system that loads interview modules and topics from JSON, validates the data using Pydantic, and exposes it through a FastAPI endpoint.

### Context

The AI Interview Agent needs a structured curriculum so that the Interview Engine can later generate questions based on different modules and topics.

### Prompt

You are a Senior Backend Engineer.

Design and implement a modular curriculum loader using JSON, Pydantic, FastAPI, and a service layer.

The system should load curriculum data from a JSON file, validate it using Pydantic models, and expose it through a REST API.

### Requirements

- Create `curriculum.json`.
- Create a Pydantic `Curriculum` model.
- Create a Pydantic `Module` model.
- Create a `CurriculumService`.
- Create a FastAPI Curriculum API route.
- Register the Curriculum router in `main.py`.
- Validate curriculum data using Pydantic.
- Expose curriculum data through a REST API.

### Implementation

Created:

```text
backend/
├── data/
│   ├── candidate.json
│   └── curriculum.json
│
└── app/
    ├── api/
    │   ├── candidate.py
    │   └── curriculum.py
    │
    ├── models/
    │   ├── candidate.py
    │   └── curriculum.py
    │
    └── services/
        ├── candidate_service.py
        └── curriculum_service.py
```

### API Endpoint

```text
GET /api/curriculum
```

---

## Prompt 9 — Interview Engine

### Goal

Build the core interview engine that manages interview questions, sessions, and candidate answers.

### Requirements

- Create InterviewQuestion model.
- Create InterviewSession model.
- Create InterviewService.
- Create mock interview questions.
- Start an interview session for a candidate.
- Retrieve questions by question number.
- Accept candidate answers.
- Return the next question.
- Detect interview completion.

### Implementation

Created:

```text
backend/
└── app/
    ├── api/
    │   └── interview.py
    │
    ├── models/
    │   └── interview.py
    │
    └── services/
        └── interview_service.py
```

### API Endpoints

```text
GET /api/interview/question/{question_number}
POST /api/interview/start
POST /api/interview/answer
```

### Current Implementation

The Interview Engine currently uses predefined mock questions.

AI-based question generation will be integrated later through the LLM/API layer.

### Engineering Reason

A separate Interview Engine makes question selection, interview sessions, answer processing, and future adaptive interview logic modular and maintainable.

## Prompt 10 — Conversation Memory

### Goal

Maintain candidate interview answers during an active interview session.

### Requirements

- Create an InterviewMemory system.
- Store candidate answers by candidate ID.
- Store question ID and candidate answer.
- Retrieve previously submitted answers.
- Clear candidate interview memory when required.
- Integrate InterviewMemory with InterviewService.
- Expose interview memory through a FastAPI endpoint.

### Implementation

Created:

```text
backend/
└── app/
    ├── api/
    │   └── interview.py
    │
    ├── memory/
    │   └── interview_memory.py
    │
    └── services/
        └── interview_service.py
    ```
```
## Prompt 11 — Follow-up Question Generator

### Goal

Generate a relevant follow-up interview question based on the candidate's previous answer.

### Requirements

* Create a FollowUpRequest model.
* Create a FollowUpResponse model.
* Create a FollowUpService.
* Accept candidate ID, previous question ID, and candidate answer.
* Analyze the candidate's answer.
* Generate a contextually relevant follow-up question.
* Return the follow-up question through a FastAPI endpoint.

### Implementation

Created:

```text
backend/
└── app/
    ├── api/
    │   └── followup.py
    │
    ├── models/
    │   └── followup.py
    │
    └── services/
        └── followup_service.py
```

### API Endpoint

```text
POST /api/followup/generate
```

### Current Implementation

The current MVP uses rule-based answer analysis to select relevant follow-up questions.

For example:

* Answers containing `list` → list vs tuple follow-up
* Answers containing `tuple` → tuple use-case follow-up
* Answers containing `function` → parameters vs arguments follow-up
* Answers containing `oop` or `object` → OOP principles follow-up
* Answers containing `exception` → exception handling follow-up

A future LLM integration can replace the rule-based logic with dynamic AI-generated follow-up questions.

### Engineering Reason

Follow-up questions make the interview more conversational and adaptive instead of simply presenting a fixed sequence of questions.

```
```
## Prompt 12 — Feedback Generator

### Goal

Generate structured interview feedback based on the candidate's submitted answers.

### Requirements

* Create a FeedbackResponse model.
* Create a FeedbackService.
* Retrieve candidate answers from InterviewMemory.
* Calculate technical score.
* Calculate communication score.
* Calculate overall score.
* Identify candidate strengths.
* Identify candidate weaknesses.
* Generate improvement recommendations.
* Return structured feedback through a FastAPI endpoint.

### Implementation

Created:

```text
backend/
└── app/
    ├── api/
    │   └── feedback.py
    │
    ├── models/
    │   └── feedback.py
    │
    └── services/
        └── feedback_service.py
```

### API Endpoint

```text
GET /api/feedback/{candidate_id}
```

### Current Implementation

The current MVP generates structured feedback using interview memory and basic scoring logic.

The feedback contains:

```text
overall_score
technical_score
communication_score
strengths
weaknesses
recommendations
```

If no interview answers are available, the API returns a zero-score response explaining that the interview must be completed first.

### Engineering Reason

A dedicated feedback service separates evaluation logic from the interview engine and provides a clear foundation for future AI-based candidate evaluation.

```
```
## Prompt 13 — Backend API Integration

### Goal

Integrate all backend modules into a unified FastAPI application and ensure that the complete interview workflow is accessible through REST APIs.

### Requirements

* Register all API routers in the FastAPI application.
* Integrate Candidate API.
* Integrate Curriculum API.
* Integrate Interview API.
* Integrate Follow-up API.
* Integrate Feedback API.
* Configure a central FastAPI application entry point.
* Verify API availability through Swagger/OpenAPI.
* Verify the interview workflow from session creation to feedback generation.
* Handle API errors using appropriate HTTP status codes.

### Implementation

The FastAPI application is configured as the central backend entry point:

```text
backend/
└── app/
    ├── main.py
    │
    ├── api/
    │   ├── candidate.py
    │   ├── curriculum.py
    │   ├── interview.py
    │   ├── followup.py
    │   └── feedback.py
    │
    ├── models/
    │   ├── candidate.py
    │   ├── curriculum.py
    │   ├── interview.py
    │   ├── followup.py
    │   └── feedback.py
    │
    ├── services/
    │   ├── candidate_service.py
    │   ├── curriculum_service.py
    │   ├── interview_service.py
    │   ├── followup_service.py
    │   └── feedback_service.py
    │
    └── memory/
        └── interview_memory.py
```

### Registered API Routers

The following routers are registered in `app/main.py`:

```text
Candidate Router
Curriculum Router
Interview Router
Follow-up Router
Feedback Router
```

### Integrated API Endpoints

```text
GET  /api/candidate

GET  /api/curriculum

GET  /api/interview/question/{question_number}
POST /api/interview/start
POST /api/interview/answer
GET  /api/interview/memory/{candidate_id}

POST /api/followup/generate

GET  /api/feedback/{candidate_id}
```

### API Verification

The backend has been successfully started using:

```bash
python -m uvicorn app.main:app --reload
```

The FastAPI Swagger documentation is available at:

```text
/docs
```

The interview start endpoint has been successfully verified using:

```text
POST /api/interview/start
```

Example successful response:

```json
{
  "candidate_id": "candidate_001",
  "current_question": {
    "id": "q1",
    "question": "What is a Python list?",
    "topic": "Python Basics",
    "difficulty": "easy"
  },
  "question_number": 1,
  "total_questions": 5
}
```

### Error Handling

The API uses FastAPI `HTTPException` handling for invalid requests and missing resources.

Examples:

```text
404 → Resource or question not found
422 → Invalid request data
```

### Current Architecture

```text
React Frontend
      │
      │ REST API
      ▼
FastAPI Application
      │
      ├── Candidate API
      │       ↓
      │   Candidate Service
      │
      ├── Curriculum API
      │       ↓
      │   Curriculum Service
      │
      ├── Interview API
      │       ↓
      │   Interview Service
      │       ↓
      │   Interview Memory
      │
      ├── Follow-up API
      │       ↓
      │   Follow-up Service
      │
      └── Feedback API
              ↓
          Feedback Service
```

### Engineering Reason

Centralizing the backend APIs through FastAPI provides a clean contract between the frontend and backend.

A modular router and service architecture keeps business logic separated from HTTP concerns and makes the system easier to test, maintain, and extend.

The current backend provides the foundation required for frontend integration and future AI/LLM integration.

## Prompt 14 — Frontend API Integration

### Goal

Connect the React frontend with the existing FastAPI backend to create a complete end-to-end interview experience.

### Context

The backend APIs and services have already been implemented and integrated into the central FastAPI application.

The backend currently provides:

* Candidate API
* Curriculum API
* Interview API
* Conversation Memory
* Follow-up API
* Feedback API

The frontend has already been configured using:

* React
* TypeScript
* Vite
* Tailwind CSS
* shadcn/ui
* Landing page components

The next step is to connect the frontend with the existing backend APIs without changing the existing backend architecture.

### Prompt

You are a Senior Full-Stack Engineer.

Integrate the existing React frontend with the FastAPI backend of the AI Interview Agent.

Implement the complete frontend interview flow:

1. Start the interview from the landing page.
2. Send the candidate ID to the backend.
3. Receive the first interview question.
4. Display the current question in the frontend.
5. Allow the candidate to enter an answer.
6. Submit the answer to the FastAPI backend.
7. Receive the next question from the backend.
8. Update the interview state and progress.
9. Continue until the interview is completed.
10. Handle the interview completion state so that the application can proceed to final feedback/results.

The frontend should maintain appropriate state for:

* Candidate ID
* Current question
* Question number
* Total questions
* Candidate answer
* Interview progress
* Loading state
* Error state
* Interview completion

Use the existing backend API contract and preserve the existing working backend modules.

Do not rewrite the backend architecture or unnecessarily modify existing working components.

### Expected Output

A working React frontend connected to the FastAPI backend.

The expected flow should be:

```text
Landing Page
      ↓
Start Interview
      ↓
POST /api/interview/start
      ↓
Question Display
      ↓
Candidate Answer
      ↓
POST /api/interview/answer
      ↓
Next Question
      ↓
Repeat
      ↓
Interview Completion
```

The frontend should successfully communicate with the backend and build successfully using the Vite production build command.

### Implementation

The frontend API integration has been implemented using the existing React/Vite/TypeScript application.

The frontend now communicates with the FastAPI interview endpoints and manages the interview state required for displaying questions and submitting candidate answers.

The existing landing page and backend architecture were preserved.

### Build Verification

The Vite production build was successfully completed.

```text
✓ 74 modules transformed
✓ built successfully
```

A Vite `__dirname` warning was observed during the build, but it did not prevent the production build from completing successfully.

### Engineering Reason

The backend APIs were already functional, but the project needed a user-facing frontend that could consume those APIs and execute the interview workflow.

Connecting the frontend and backend transforms the separate frontend and backend components into a functional interview application while keeping the existing modular architecture intact.

This integration also provides the foundation for the next stage: the final feedback and results dashboard.

# Prompt 15 — Final Feedback & Results Dashboard

## Goal

Create a final feedback and results dashboard that displays the candidate's interview performance after completing the interview.

## Context

The interview flow and backend feedback service are already implemented.

The frontend now needs to display the final interview results after the candidate completes all interview questions.

The dashboard should consume the existing Feedback API without changing the existing backend architecture.

## Prompt

You are a Senior Full-Stack Engineer.

Implement a final interview feedback and results dashboard for the AI Interview Agent.

The system should:

1. Detect when the interview is completed.
2. Transition from the interview screen to the results dashboard.
3. Request the candidate's feedback from the backend.
4. Display the overall interview score.
5. Display the technical score.
6. Display the communication score.
7. Display candidate strengths.
8. Display areas for improvement.
9. Display learning recommendations.
10. Handle loading and error states.

Preserve the existing React/Vite/TypeScript frontend architecture and FastAPI backend architecture.

## Expected Output

The expected flow should be:

```text
Interview
    ↓
Submit Final Answer
    ↓
Interview Completed
    ↓
Feedback API
    ↓
Results Dashboard
```

The dashboard should provide a clear summary of the candidate's interview performance.

## Implementation

Created:

```text
frontend/
└── src/
    ├── App.tsx
    ├── pages/
    │   ├── Interview.tsx
    │   └── Dashboard.tsx
    └── services/
        └── api.ts
```

### Dashboard

The `Dashboard.tsx` component:

* Fetches feedback using the candidate ID.
* Displays overall score.
* Displays technical score.
* Displays communication score.
* Displays strengths.
* Displays weaknesses.
* Displays learning recommendations.
* Handles loading state.
* Handles API error state.

### Interview Completion

The `Interview.tsx` component now supports an `onComplete` callback.

When the backend returns:

```json
{
  "completed": true
}
```

the interview completion callback is triggered.

`App.tsx` then transitions the application to the feedback dashboard.

### Feedback API

The frontend integrates with the backend feedback endpoint through the API service.

The frontend maintains the existing API client architecture and does not modify the backend service structure.

## Verification

The complete frontend production build was successfully verified using:

```bash
npm run build
```

Build result:

```text
✓ 76 modules transformed
✓ built successfully
```

A Vite `__dirname` warning was observed, but it did not prevent the production build from completing successfully.

## Engineering Reason

The feedback dashboard completes the end-to-end candidate experience.

Previously, the system could conduct the interview and generate backend feedback, but the candidate did not have a dedicated frontend interface for viewing the final results.

The dashboard connects interview completion with the feedback service and provides a user-facing performance report.

This also creates a foundation for future improvements such as AI-generated evaluation, per-question analysis, performance charts, and personalized recommendations.
