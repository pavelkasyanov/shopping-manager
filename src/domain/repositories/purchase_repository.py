from src.domain.models.purchase import Purchase
from src.domain.wrappers.transactional_wrapper import transactional


class PurchaseRepository:

    @transactional
    def get_all(self, session=None):
        return session.query(Purchase).all()