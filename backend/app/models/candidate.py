from pydantic import BaseModel, EmailStr


class Education(BaseModel):
    degree: str
    graduation_year: int


class Candidate(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str
    experience_level: str
    skills: list[str]
    education: Education