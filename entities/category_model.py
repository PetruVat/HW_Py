from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db

class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        db.String(60),
        nullable=False,
        unique=True
    )

    questions: Mapped["Question"] = relationship("Question", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category {self.id}: {self.name}>"
