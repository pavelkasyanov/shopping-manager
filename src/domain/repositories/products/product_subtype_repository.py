from src.domain.models.products.product_subtype import ProductSubType
from src.domain.wrappers.transactional_wrapper import transactional


class ProductSubTypeRepository:
    @transactional
    def get_all(self, session=None):
        return session.query(ProductSubType).all()