from typing import Optional
from uuid import UUID

from app.domain.models.base import Entity


class CreateProductModel(Entity):
    name: str
    remark: Optional[str] = None
    type_id: UUID
    subtype_id: UUID


class ProductModel(CreateProductModel):
    id: UUID

    class Config:
        orm_mode = True


class CreateProductTypeModel(Entity):
    name: str
    remark: Optional[str] = None


class ProductTypeModel(CreateProductTypeModel):
    id: UUID

    class Config:
        orm_mode = True


class CreateProductSubTypeModel(Entity):
    name: str
    product_type_id: UUID
    remark: Optional[str] = None


class ProductSubTypeModel(CreateProductSubTypeModel):
    id: UUID

    class Config:
        orm_mode = True
