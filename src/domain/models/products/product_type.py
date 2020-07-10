from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, backref

from src.domain import Base


class ProductType(Base):
    __tablename__ = 'product_types'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
