from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database.db import db


class ProductType(db.Model):
    __tablename__ = "product_types"

    id = db.Column(UUID, primary_key=True, unique=True, index=True, nullable=False, default=uuid4)
    name = db.Column(db.String, nullable=False)
    remark = db.Column(db.String, nullable=True)
