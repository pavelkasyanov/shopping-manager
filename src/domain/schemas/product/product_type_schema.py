from marshmallow import fields, post_load

from src.domain.dto.products.product_type_dto import ProductTypeDto
from src.domain.schemas.base_schema import BaseSchema


class ProductTypeSchema(BaseSchema):
    id = fields.UUID(required=False)
    name = fields.Str(required=True, allow_none=False, dump_to="name", load_from="name")

    @post_load
    def make_user(self, data):
        return ProductTypeDto(**data)
