from marshmallow import fields, post_load

from src.domain.dto.products.product_subtype_dto import ProductSubTypeDto
from src.domain.schemas.base_schema import BaseSchema


class ProductSubTypeSchema(BaseSchema):
    id = fields.UUID(required=False)
    name = fields.Str(required=True, allow_none=False, dump_to="name", load_from="name")
    product_type_id = fields.UUID(required=True, allow_none=False,
                                  dump_to="productTypeId",
                                  load_from="productTypeId")

    @post_load
    def make_user(self, data):
        return ProductSubTypeDto(**data)
