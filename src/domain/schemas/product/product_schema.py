from marshmallow import fields, post_load, validates

from src.domain.dto.products.product_dto import ProductDto
from src.domain.schemas.base_schema import BaseSchema


class ProductSchema(BaseSchema):
    id = fields.UUID(required=False)
    purchase_id = fields.UUID(required=True, allow_none=False, dump_to="purchaseId", load_from="purchaseId")
    type_id = fields.UUID(required=True, allow_none=False, dump_to="typeId", load_from="typeId")
    subtype_id = fields.UUID(required=True, allow_none=False, dump_to="subTypeId", load_from="subTypeId")

    count = fields.Int(required=True, allow_none=False, validate=lambda x: x > 0.0)
    unit_price = fields.Float(required=True, allow_none=False,
                              dump_to="unitPrice",
                              load_from="unitPrice",
                              validate=lambda x: x > 0.0)
    unit_price_with_discount = fields.Float(required=True, allow_none=False,
                                            dump_to="unitPriceWithDiscount",
                                            load_from="unitPriceWithDiscount",
                                            validate=lambda x: x >= 0.0)
    remark = fields.Str(required=False, allow_none=True)

    @post_load
    def make_user(self, data):
        return ProductDto(**data)
