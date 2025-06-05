from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# 1.1  Схема для вложенной категории

class CategoryBase(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class QuestionDTO(BaseModel):
    id: int
    text: str
    category: Optional[CategoryBase] = None

    model_config = ConfigDict(from_attributes=True)

class QuestionCreateDTO(BaseModel):
    text: str = Field(..., min_length=10)
    category_id: Optional[int] = Field(None, gt=0)
