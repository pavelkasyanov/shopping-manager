from sqlalchemy import Column, ForeignKey, String, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship, backref

from src.domain import Base


class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    date = Column(DateTime, nullable=False)
    cashbox_number = Column(Integer, nullable=True)
    cashier_name = Column(String, nullable=True)
    total_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, nullable=False)

    purchase_place_id = Column(ForeignKey('purchase_places.id', ondelete='CASCADE'), nullable=True)

    purchase_place = relationship('PurchasePlace', primaryjoin='Purchase.purchase_place_id == PurchasePlace.id')
    goods = relationship('ProductToBuy', primaryjoin='ProductToBuy.purchase_id == Purchase.id')
