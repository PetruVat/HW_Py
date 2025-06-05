from flask import Blueprint, jsonify, request
from services.category_service import (
    list_categories,
    create_category,
    get_category,
    update_category,
    remove_category,
)
from serializers.category_schema import CategoryDTO

category_bp = Blueprint("categories", __name__)

@category_bp.route("", methods=["GET", "POST"])
def categories_collection():
    if request.method == "GET":
        cats = list_categories()
        return jsonify([CategoryDTO.model_validate(c).model_dump() for c in cats])

    if request.method == "POST":
        created = create_category(request.json or {})
        return (
            jsonify(CategoryDTO.model_validate(created).model_dump()),
            201,
        )

@category_bp.route("/<int:cat_id>", methods=["GET", "PUT", "DELETE"])
def category_detail(cat_id: int):
    cat = get_category(cat_id)

    if request.method == "GET":
        return jsonify(CategoryDTO.model_validate(cat).model_dump())

    if request.method == "PUT":
        updated = update_category(cat, request.json or {})
        return jsonify(CategoryDTO.model_validate(updated).model_dump())

    if request.method == "DELETE":
        remove_category(cat)
        return "", 204
