from typing import List
from uuid import UUID

from src.domain.models.products.product import Product
from src.domain.wrappers.transactional_wrapper import transactional


class ProductRepository:
    @transactional
    def get_all(self, session=None):
        return session.query(Product).all()

    @transactional
    def get_from_purchase(self, purchase_id: UUID, session=None):
        pass

    @transactional
    def create_product(self, product: Product, session=None) -> Product or None:
        pass

    @transactional
    def create_products(self, product: List[Product], session=None) -> List[Product] or None:
        pass

    @transactional
    def edit_product(self, product: Product, session=None) -> Product or None:
        pass

    @transactional
    def delete_product(self, product_id: UUID) -> None:
        pass
