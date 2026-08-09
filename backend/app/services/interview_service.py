from app.models.interview import InterviewQuestion, InterviewSession
from app.memory.interview_memory import interview_memory
from app.ai.llm_service import LLMService


class InterviewService:

    def __init__(self):

        # Use the single shared interview memory
        self.memory = interview_memory

        # Use the configured AI provider through LLMService
        self.llm_service = LLMService()

        self.questions = [
            InterviewQuestion(
                id="q1",
                question="What is a Python list?",
                topic="Python Basics",
                difficulty="easy"
            ),
            InterviewQuestion(
                id="q2",
                question="What is the difference between a list and a tuple in Python?",
                topic="Data Types",
                difficulty="medium"
            ),
            InterviewQuestion(
                id="q3",
                question="What is a function in Python and why is it useful?",
                topic="Functions",
                difficulty="easy"
            ),
            InterviewQuestion(
                id="q4",
                question="What is Object-Oriented Programming?",
                topic="Object Oriented Programming",
                difficulty="medium"
            ),
            InterviewQuestion(
                id="q5",
                question="How does exception handling work in Python?",
                topic="Exception Handling",
                difficulty="medium"
            )
        ]

    def get_question(self, question_number: int) -> InterviewQuestion:

        index = question_number - 1

        if index < 0 or index >= len(self.questions):
            raise IndexError("Question number out of range")

        return self.questions[index]

    def get_total_questions(self) -> int:
        return len(self.questions)

    def generate_ai_question(
        self,
        topic: str,
        difficulty: str,
        role: str = "Python Developer",
        experience_level: str = "Beginner",
        skills: str = "Python"
    ) -> str:
        """
        Generate an interview question using the configured AI provider.
        """

        context = {
            "role": role,
            "experience_level": experience_level,
            "skills": skills,
            "topic": topic,
            "difficulty": difficulty
        }

        return self.llm_service.generate_question(context)

    def start_interview(self, candidate_id: str) -> InterviewSession:

        # Clear previous interview data
        self.memory.clear_memory(candidate_id)

        # Generate first question using AI
        first_question_text = self.generate_ai_question(
            topic="Python Basics",
            difficulty="easy",
            role="Python Developer",
            experience_level="Beginner",
            skills="Python"
        )

        # Replace fixed Q1 with AI-generated Q1
        self.questions[0] = InterviewQuestion(
            id="ai_q1",
            question=first_question_text,
            topic="Python Basics",
            difficulty="easy"
        )

        first_question = self.questions[0]

        return InterviewSession(
            candidate_id=candidate_id,
            current_question=first_question,
            question_number=1,
            total_questions=self.get_total_questions()
        )

    def submit_answer(
        self,
        candidate_id: str,
        question_id: str,
        answer: str
    ):

        current_question_number = None

        for index, question in enumerate(self.questions):

            if question.id == question_id:
                current_question_number = index + 1
                break

        if current_question_number is None:
            raise ValueError("Question not found")

        # Save answer in shared memory
        self.memory.add_answer(
            candidate_id=candidate_id,
            question_id=question_id,
            answer=answer
        )

        next_question_number = current_question_number + 1

        if next_question_number > self.get_total_questions():

            return {
                "candidate_id": candidate_id,
                "question_id": question_id,
                "answer": answer,
                "next_question": None,
                "completed": True
            }

        next_question = self.get_question(next_question_number)

        return {
            "candidate_id": candidate_id,
            "question_id": question_id,
            "answer": answer,
            "next_question": next_question,
            "completed": False
        }

    def get_interview_memory(self, candidate_id: str):

        return self.memory.get_answers(candidate_id)
