from pydantic import BaseModel, Field, ConfigDict

class CategoryDTO(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class CategoryCreateDTO(BaseModel):
    name: str = Field(..., min_length=2, max_length=60)
