import datetime

import pytest
from fastapi_jwt_auth import AuthJWT
from httpx import AsyncClient

from app.app import app
from app.domain.models.auth_user_claims import AuthUserClaims
from app.domain.models.user_schemas import VerificationUserSchema
from app.domain.services.authentication_service import AuthenticationService


@pytest.fixture()
def authorize():
    return AuthJWT()


@pytest.fixture
async def async_client() -> AsyncClient:
    client = AsyncClient(app=app, base_url="http://test.by")
    yield client
    await client.aclose()


@pytest.fixture
async def auth_client(async_client, mocker, authorize) -> AsyncClient:
    async def response(*args, **kwargs) -> VerificationUserSchema:
        return VerificationUserSchema(
            user_id=2,
            password="passwd",
            created_date=datetime.datetime.utcnow(),
            nickname="test",
            email="test@test.com",
            is_superuser=False,
        )

    mocker.patch.object(
        AuthenticationService, "verify_user", side_effect=response
    )
    user_claims = AuthUserClaims(user_id=2, is_superuser=False).dict()
    access_token = authorize.create_access_token(
        "test@test.com", user_claims=user_claims
    )
    async_client.headers["Authorization"] = f"Bearer {access_token}"

    yield async_client


@pytest.fixture
async def auth_superuser_client(async_client, mocker, authorize) -> AsyncClient:
    async def response(*args, **kwargs) -> VerificationUserSchema:
        return VerificationUserSchema(
            user_id=1,
            password="passwd_super",
            created_date=datetime.datetime.utcnow(),
            nickname="test_super",
            email="test_super@test.com",
            is_superuser=True,
        )

    mocker.patch.object(
        AuthenticationService, "verify_user", side_effect=response
    )

    user_claims = AuthUserClaims(user_id=1, is_superuser=True).dict()
    access_token = authorize.create_access_token(
        "test@test.com", user_claims=user_claims
    )
    async_client.headers["Authorization"] = f"Bearer {access_token}"

    yield async_client
