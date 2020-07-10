from uuid import UUID

from injector import inject

from src.domain.dto.purchase_dto import PurchaseDto
from src.domain.repositories.products.product_repository import ProductRepository
from src.domain.repositories.purchase_repository import PurchaseRepository


class PurchaseService:
    @inject
    def __init__(self, purchase_repository: PurchaseRepository,
                 product_repository: ProductRepository):
        self._purchase_repository = purchase_repository
        self._product_repository = product_repository

    def get_all(self, user_id: UUID) -> PurchaseDto:
        pass
