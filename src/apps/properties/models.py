from pydantic import BaseModel, Field


class Property(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    image: str

    class Config:
        orm_mode = True


class CreateProperty(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    image: str
