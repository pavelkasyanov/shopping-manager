from marshmallow import Schema, fields, post_load, validates

from src.domain.dto.purchase_dto import PurchaseDto
from src.domain.dto.purchase_place_dto import PurchasePlaceDto
from src.domain.schemas.base_schema import BaseSchema


class PurchasePlaceSchema(BaseSchema):
    id = fields.UUID(required=False)
    name = fields.Str(required=False, allow_none=False, dump_to="name", load_from="name")
    address = fields.Str(required=True, allow_none=True, dump_to="address", load_from="address")

    @post_load
    def make_user(self, data):
        return PurchasePlaceDto(**data)
