from typing import Optional
from pydantic import BaseModel

class VaccinationBaseSchema(BaseModel):
    local: str
    atendimento: str
    publico: str

class VaccinationSchema(VaccinationBaseSchema):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class VaccinationCreateSchema(VaccinationBaseSchema):
    pass

class CityBaseSchema(BaseModel):
    name: str

class CitySchema(CityBaseSchema):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class CityCreateSchema(CityBaseSchema):
    pass