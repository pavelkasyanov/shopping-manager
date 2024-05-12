from typing import Callable, Optional

import pytest as pytest

from app.domain.deps import Services
from app.domain.models.products_schemas import ProductTypeModel
from app.domain.repositories.tests.fixtures import CreateProductTypeFixture

repo = Services.product_type_repository


@pytest.mark.asyncio
async def test_gel_all_product_types_empty_success() -> None:
    result = await repo.get_all()
    assert len(result) == 0


@pytest.mark.asyncio
@pytest.mark.parametrize("remark", (None, "test_product_type_remark"))
async def test_create_product_type_success(
    create_product_type: CreateProductTypeFixture, remark: Optional[str]
) -> None:
    product_type_name = "test_product_type_name"
    created_product_type = await create_product_type(product_type_name, remark)

    assert created_product_type is not None
    assert created_product_type.id is not None
    assert created_product_type.name == product_type_name
    assert created_product_type.remark == remark


@pytest.mark.asyncio
@pytest.mark.parametrize("remark", (None, "test_product_type_remark"))
async def test_update_product_type_success(
    create_product_type: CreateProductTypeFixture, remark: Optional[str]
) -> None:
    product_type_name = "test_product_type_name"
    created_product_type = await create_product_type("test_product", remark)

    assert created_product_type is not None
    assert created_product_type.id is not None

    product_type_model = ProductTypeModel(id=str(created_product_type.id), name=product_type_name, remark=remark)
    updated_product = await repo.update(product_type_model)

    product = await repo.get_by_id(product_type_model.id)

    assert updated_product is not None
    assert updated_product.id == created_product_type.id
    assert updated_product.name == product_type_name
    assert updated_product.remark == remark
