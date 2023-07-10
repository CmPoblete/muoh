from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from src.db.sqlalchemy import Base


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String)
    image: Mapped[str] = Column(String)
