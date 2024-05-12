from typing import Type

from app.domain.models.products_schemas import CreateProductModel, ProductModel
from app.domain.repositories.base_crud_repository import BaseCRUDRepository
from app.infrastructure.database.models.product import Product


class ProductRepository(BaseCRUDRepository[Type[Product], CreateProductModel, ProductModel]):
    _model = Product
