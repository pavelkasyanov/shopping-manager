import pytest as pytest

from app.domain.deps import Services
from app.domain.models.products_schemas import CreateProductModel
from app.infrastructure.database.models.product import Product


async def create_product() -> Product:
    repo = Services.product_repository
    create_product_model = CreateProductModel()


@pytest.mark.asyncio
async def test_gel_all_products_empty_success() -> None:
    repo = Services.product_repository

    result = await repo.get_all()
    assert len(result) == 0
