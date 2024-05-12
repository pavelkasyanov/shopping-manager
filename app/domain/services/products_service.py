from typing import List, Type

from app.domain.models.products_schemas import ProductModel, ProductSubTypeModel, ProductTypeModel
from app.domain.repositories.base_crud_repository import BaseCRUDRepository, Model
from app.domain.repositories.product_repository import ProductRepository
from app.domain.repositories.product_subtype_repository import ProductSubTypeRepository
from app.domain.repositories.product_type_repository import ProductTypeRepository


async def _get_all(repo: BaseCRUDRepository, model: Type[Model]) -> List[Model]:
    data = await repo.get_all()
    return [model.from_orm(x) for x in data]


class ProductsService:
    def __init__(
        self,
        product_repository: ProductRepository,
        product_type_repository: ProductTypeRepository,
        product_subtype_repository: ProductSubTypeRepository,
    ) -> None:
        self._product_repository = product_repository
        self._product_type_repository = product_type_repository
        self._product_subtype_repository = product_subtype_repository

    async def get_all_product_types(self) -> List[ProductTypeModel]:
        return await _get_all(self._product_type_repository, ProductTypeModel)

    async def get_all_product_sub_types(self) -> List[ProductSubTypeModel]:
        return await _get_all(self._product_subtype_repository, ProductSubTypeModel)

    async def get_all_products(self) -> List[ProductModel]:
        return await _get_all(self._product_repository, ProductModel)
