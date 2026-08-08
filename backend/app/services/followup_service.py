from app.models.followup import FollowUpResponse


class FollowUpService:

    def generate_follow_up(
        self,
        candidate_id: str,
        question_id: str,
        answer: str
    ) -> FollowUpResponse:

        answer_lower = answer.lower()

        if "list" in answer_lower:
            question = (
                "Can you explain the difference between a Python list "
                "and a tuple?"
            )

        elif "tuple" in answer_lower:
            question = (
                "Why would you choose a tuple instead of a list "
                "in Python?"
            )

        elif "function" in answer_lower:
            question = (
                "Can you explain the difference between parameters "
                "and arguments in a Python function?"
            )

        elif "oop" in answer_lower or "object" in answer_lower:
            question = (
                "Can you explain the four main principles of "
                "Object-Oriented Programming?"
            )

        elif "exception" in answer_lower:
            question = (
                "What is the difference between try-except and "
                "try-finally in Python?"
            )

        else:
            question = (
                "Can you explain your answer with a practical "
                "example?"
            )

        return FollowUpResponse(
            candidate_id=candidate_id,
            previous_question_id=question_id,
            follow_up_question=question
        )