from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, backref

from src.domain import Base


class ProductSubType(Base):
    __tablename__ = 'product_subtypes'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)

    product_type_id = Column(ForeignKey('product_types.id', ondelete='CASCADE'), index=True)

    product_type = relationship('ProductType', primaryjoin='ProductSubType.product_type_id == ProductType.id',
                                backref=backref('subtypes', cascade="all, delete"))
