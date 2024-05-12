from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database.db import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(UUID, primary_key=True, unique=True, index=True, nullable=False, default=uuid4)
    name = db.Column(db.String, nullable=False)
    remark = db.Column(db.String, nullable=True)
    type_id = db.Column(UUID, db.ForeignKey("types.id"))
    subtype_id = db.Column(UUID, db.ForeignKey("subtypes.id"))
    archived = db.Column(db.Boolean, nullable=False, default=False)
