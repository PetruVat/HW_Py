from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db

class Question(db.Model):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(db.String(255), nullable=False)
    category_id: Mapped[int | None] = mapped_column(db.Integer, db.ForeignKey("categories.id"), nullable=True)

    category: Mapped["Category"] = relationship("Category", back_populates="questions")
    answers: Mapped["Answer"] = relationship("Answer", back_populates="question")

    def __repr__(self) -> str:
        return f"<Question {self.id}>"
