from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField
from bson.objectid import ObjectId


class Property(BaseModel):
    id: int | ObjectIdField = Field(alias="_id")
    name: str = Field(min_length=3, max_length=50)
    image: str

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        fields = {"_id": "id"}


class CreateProperty(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    image: str
