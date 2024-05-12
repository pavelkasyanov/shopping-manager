from typing import Type

from app.domain.models.products_schemas import CreateProductTypeModel, ProductTypeModel
from app.domain.repositories.base_crud_repository import BaseCRUDRepository
from app.infrastructure.database.models.product_type import ProductType


class ProductTypeRepository(BaseCRUDRepository[Type[ProductType], CreateProductTypeModel, ProductTypeModel]):
    _model = ProductType
