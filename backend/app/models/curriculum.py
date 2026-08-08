from pydantic import BaseModel


class Module(BaseModel):
    id: str
    name: str
    topics: list[str]


class Curriculum(BaseModel):
    course: str
    modules: list[Module]