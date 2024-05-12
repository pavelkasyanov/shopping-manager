from typing import List

from fastapi import APIRouter, Depends

from app.api.deps import get_products_service
from app.domain.models.products_schemas import ProductModel, ProductSubTypeModel, ProductTypeModel
from app.domain.services.products_service import ProductsService

router = APIRouter(prefix="/products")


@router.get("/", name="get_all_products", status_code=200)
async def get_all_products(
    products_service: ProductsService = Depends(get_products_service),
) -> List[ProductModel]:
    return await products_service.get_all_products()


@router.get("/product_types", name="get_all_product_types", status_code=200)
async def get_all_product_types(
    products_service: ProductsService = Depends(get_products_service),
) -> List[ProductTypeModel]:
    return await products_service.get_all_product_types()


@router.get("/product_subtypes", name="get_all_product_subtypes", status_code=200)
async def get_all_product_subtypes(
    products_service: ProductsService = Depends(get_products_service),
) -> List[ProductSubTypeModel]:
    return await products_service.get_all_product_sub_types()
