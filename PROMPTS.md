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