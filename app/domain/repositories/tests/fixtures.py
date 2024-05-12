from typing import Awaitable, Callable, Optional

import pytest

from app.domain.deps import Services
from app.domain.models.products_schemas import CreateProductSubTypeModel, CreateProductTypeModel
from app.domain.types import ProductTypeId
from app.infrastructure.database.models.product_sub_type import ProductSubType
from app.infrastructure.database.models.product_type import ProductType

CreateProductTypeFixture = Callable[[str, Optional[str]], Awaitable[ProductType]]


@pytest.fixture
async def create_product_type() -> CreateProductTypeFixture:
    async def wrapper(name: str, remark: Optional[str] = None) -> ProductType:
        create_product_model = CreateProductTypeModel(name=name, remark=remark)
        return await Services.product_type_repository.create(create_product_model)

    return wrapper


CreateProductSubTypeFixture = Callable[[str, ProductTypeId, Optional[str]], Awaitable[ProductSubType]]


@pytest.fixture
async def create_product_sub_type() -> CreateProductSubTypeFixture:
    async def wrapper(name: str, product_type_id: ProductTypeId, remark: Optional[str] = None) -> ProductSubType:
        create_product_sub_type_model = CreateProductSubTypeModel(
            name=name, product_type_id=product_type_id, remark=remark
        )
        return await Services.product_subtype_repository.create(create_product_sub_type_model)

    return wrapper
