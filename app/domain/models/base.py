from pydantic.main import BaseModel


class Entity(BaseModel):
    class Config:
        allow_population_by_field_name = True
