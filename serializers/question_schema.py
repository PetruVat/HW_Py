from pydantic import BaseModel, Field, ConfigDict

class QuestionDTO(BaseModel):
    id: int
    text: str
    category_id: int | None = None

    model_config = ConfigDict(from_attributes=True)

class QuestionCreateDTO(BaseModel):
    text: str = Field(..., min_length=10)
    category_id: int | None = Field(None, gt=0)
