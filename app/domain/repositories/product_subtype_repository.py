from typing import Type

from app.domain.models.products_schemas import CreateProductSubTypeModel, ProductSubTypeModel
from app.domain.repositories.base_crud_repository import BaseCRUDRepository
from app.infrastructure.database.models.product_sub_type import ProductSubType


class ProductSubTypeRepository(
    BaseCRUDRepository[Type[ProductSubType], CreateProductSubTypeModel, ProductSubTypeModel]
):
    _model = ProductSubType
