import json
from pathlib import Path

from app.models.curriculum import Curriculum


class CurriculumService:

    def __init__(self):
        self.data_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "curriculum.json"
        )

    def get_curriculum(self) -> Curriculum:
        with open(self.data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Curriculum(**data)