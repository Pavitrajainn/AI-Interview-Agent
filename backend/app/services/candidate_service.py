import json
from pathlib import Path

from app.models.candidate import Candidate


class CandidateService:

    def __init__(self):
        self.data_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "candidate.json"
        )

    def get_candidate(self) -> Candidate:
        with open(self.data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Candidate(**data)