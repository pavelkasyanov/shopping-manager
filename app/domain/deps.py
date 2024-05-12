from typing import cast

from dependencies import Injector

from app.domain.repositories.product_repository import ProductRepository
from app.domain.repositories.product_subtype_repository import ProductSubTypeRepository
from app.domain.repositories.product_type_repository import ProductTypeRepository
from app.domain.repositories.user_repository import UserRepository
from app.domain.services.authentication_service import AuthenticationService
from app.domain.services.products_service import ProductsService
from app.domain.services.users_service import UserService


class Services(Injector):
    user_repository = cast(UserRepository, UserRepository)
    user_service = cast(UserService, UserService)
    authentication_service = cast(AuthenticationService, AuthenticationService)
    products_service = cast(ProductsService, ProductsService)
    product_repository = cast(ProductRepository, ProductRepository)
    product_type_repository = cast(ProductTypeRepository, ProductTypeRepository)
    product_subtype_repository = cast(ProductSubTypeRepository, ProductSubTypeRepository)
