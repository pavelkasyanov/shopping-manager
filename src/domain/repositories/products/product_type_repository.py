from src.domain.models.products.product_type import ProductType
from src.domain.wrappers.transactional_wrapper import transactional


class ProductTypeRepository:
    @transactional
    def get_all(self, session=None):
        return session.query(ProductType).all()