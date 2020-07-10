from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, backref

from src.domain import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True)

    type_id = Column(ForeignKey('product_types.id', ondelete='CASCADE'), index=True)
    subtype_id = Column(ForeignKey('product_subtypes.id', ondelete='CASCADE'), index=True)
    remark = Column(String, nullable=True)

    type = relationship('ProductType', primaryjoin='Product.type_id == ProductType.id',
                        backref=backref('products', cascade="all, delete"))

    subtype = relationship('ProductSubType', primaryjoin='Product.subtype_id == ProductSubType.id',
                           backref=backref('products', cascade="all, delete"))
