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

        self._answers[candidate_id].append({
            "question_id": question_id,
            "answer": answer
        })

    def get_answers(self, candidate_id: str):
        return self._answers.get(candidate_id, [])

    def clear_memory(self, candidate_id: str):
        self._answers.pop(candidate_id, None)


# Single shared memory instance
interview_memory = InterviewMemory()