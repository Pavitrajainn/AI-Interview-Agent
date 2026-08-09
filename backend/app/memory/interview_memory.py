class InterviewMemory:

    def __init__(self):
        self._answers = {}

    def add_answer(
        self,
        candidate_id: str,
        question_id: str,
        answer: str
    ):
        if candidate_id not in self._answers:
            self._answers[candidate_id] = []

        answers = self._answers[candidate_id]

        # Prevent duplicate answers for the same question.
        for existing_answer in answers:
            if existing_answer["question_id"] == question_id:
                existing_answer["answer"] = answer
                return

        answers.append({
            "question_id": question_id,
            "answer": answer
        })

    def get_answers(self, candidate_id: str):
        return self._answers.get(candidate_id, [])

    def clear_memory(self, candidate_id: str):
        self._answers.pop(candidate_id, None)


# Single shared memory instance
interview_memory = InterviewMemory()