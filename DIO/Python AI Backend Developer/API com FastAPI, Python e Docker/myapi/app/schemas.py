from pydantic import BaseModel

class AthleteBase(BaseModel):
    name: str
    cpf: str

class AthleteCreate(AthleteBase):
    training_center: str
    category: str

class AthleteDisplay(BaseModel):
    name: str
    training_center: str
    category: str

    class Config:
        orm_mode = True
