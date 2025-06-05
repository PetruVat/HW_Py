from typing import List
from database import db
from entities.category_model import Category
from serializers.category_schema import CategoryCreateDTO

def list_categories() -> List[Category]:
    return Category.query.all()

def create_category(raw_data: dict) -> Category:
    dto = CategoryCreateDTO.model_validate(raw_data)
    new_cat = Category(name=dto.name)
    db.session.add(new_cat)
    db.session.commit()
    return new_cat

def get_category(category_id: int) -> Category | None:
    return Category.query.get_or_404(category_id)

def update_category(category_obj: Category, raw_data: dict) -> Category:
    dto = CategoryCreateDTO.model_validate(raw_data)
    category_obj.name = dto.name
    db.session.commit()
    return category_obj

def remove_category(category_obj: Category) -> None:
    db.session.delete(category_obj)
    db.session.commit()
