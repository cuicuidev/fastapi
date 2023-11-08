from pydantic import BaseModel

class Entry(BaseModel):
    id: int # PK
    exercise_id: int # FK

    n_repetitions: int
    weight_kg: float
    
    performed: int # unix timestamp

class Exercise(BaseModel):
    id: int
    name: str # exercise name