from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, backref

from src.domain import Base


class ProductToBuy(Base):
    __tablename__ = 'products_to_buy'

    id = Column(UUID(as_uuid=True), primary_key=True)
    count = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    unit_price_with_discount = Column(Float, nullable=False)

    purchase_id = Column(ForeignKey('purchases.id', ondelete='CASCADE'), index=False)
    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), index=False)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
