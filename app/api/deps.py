from app.domain.deps import Services
from app.domain.services.users_service import UserService


def get_user_service() -> UserService:
    return Services.user_service