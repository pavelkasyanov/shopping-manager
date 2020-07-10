from marshmallow import Schema, fields, post_load, validates

from src.domain.dto.purchase_dto import PurchaseDto
from src.domain.schemas.base_schema import BaseSchema


class PurchaseSchema(BaseSchema):
    id = fields.UUID(required=False)
    date = fields.DateTime(required=True, allow_none=False)
    cashbox_number = fields.Int(required=False, allow_none=True, dump_to="cashboxNumber", load_from="cashboxNumber",
                                validate=lambda x: (x is None) or (x and x > 0))
    cashier_name = fields.Str(required=False, dump_to="cashierName", load_from="cashierName")

    total_amount = fields.Float(required=False, dump_only=True, dump_to="totalAmount")
    discount_amount = fields.Float(required=False, dump_only=True, dump_to="discountAmount")

    @post_load
    def make_user(self, data):
        return PurchaseDto(**data)
