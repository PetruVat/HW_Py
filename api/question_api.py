from flask import Blueprint, jsonify, request
from services.question_service import (
    list_questions,
    create_question,
    get_question,
    update_question,
)
from serializers.question_schema import QuestionDTO, QuestionCreateDTO

question_bp = Blueprint("questions", __name__)

@question_bp.route("", methods=["GET", "POST"])
def questions_collection():
    if request.method == "GET":
        qs = list_questions()
        return jsonify([
            QuestionDTO.model_validate(q).model_dump()
            for q in qs
        ])

    if request.method == "POST":
        raw = request.json or {}
        dto = QuestionCreateDTO.model_validate(raw)
        created = create_question(dto.model_dump())
        return jsonify(QuestionDTO.model_validate(created).model_dump()), 201

@question_bp.route("/<int:question_id>", methods=["GET", "PUT"])
def question_detail(question_id: int):
    q = get_question(question_id)

    if request.method == "GET":
        return jsonify(QuestionDTO.model_validate(q).model_dump())

    if request.method == "PUT":
        updated = update_question(q, request.json or {})
        return jsonify(QuestionDTO.model_validate(updated).model_dump())
