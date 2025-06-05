from typing import List
from database import db
from entities.question_model import Question
from services.category_service import get_category
from serializers.question_schema import QuestionCreateDTO

def list_questions() -> List[Question]:
    return Question.query.all()

def create_question(raw_data: dict) -> Question:
    dto = QuestionCreateDTO.model_validate(raw_data)
    if dto.category_id:
        get_category(dto.category_id)  # raises 404 if not found
    new_q = Question(text=dto.text, category_id=dto.category_id)
    db.session.add(new_q)
    db.session.commit()
    return new_q

def get_question(question_id: int) -> Question | None:
    return Question.query.get_or_404(question_id)

def update_question(question_obj: Question, raw_data: dict) -> Question:
    dto = QuestionCreateDTO.model_validate(raw_data)
    question_obj.text = dto.text
    question_obj.category_id = dto.category_id
    db.session.commit()
    return question_obj
