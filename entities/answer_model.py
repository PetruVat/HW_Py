from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db

class Answer(db.Model):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("questions.id"))
    is_agree: Mapped[bool] = mapped_column(db.Boolean, nullable=False)

    question: Mapped["Question"] = relationship("Question", back_populates="answers")

    def __repr__(self) -> str:
        return f"<Answer {self.id} agree={self.is_agree}>"
