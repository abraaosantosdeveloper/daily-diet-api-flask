import datetime
from app import db
from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Meal(db.Model):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    is_diet: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False, 
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    
    userId: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="meals")