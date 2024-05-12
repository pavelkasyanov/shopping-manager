from typing import Generic, List, NewType, TypeVar

from app.domain.models.base import Entity
from app.domain.types import NotFoundError
from app.infrastructure.database.db import db

EntityId = NewType("EntityId", str)
EntityModel = TypeVar("EntityModel", bound=db.Model)

CreateModel = TypeVar("CreateModel", bound=Entity)
Model = TypeVar("Model", bound=Entity)


class BaseCRUDRepository(Generic[EntityModel, CreateModel, Model]):
    _model: EntityModel

    async def get_all(self) -> List[Model]:
        return await self._model.query.gino.all()

    async def get_by_id(self, entity_id: EntityId) -> EntityModel:
        entity = await self._model.get(entity_id)
        if not entity:
            raise NotFoundError()
        return entity

    async def create(self, create_model: CreateModel) -> EntityModel:
        return await self._model.create(**create_model.__dict__)

    async def update(self, new_model: Model) -> EntityModel:
        old_model = await self.get_by_id(new_model.id)  # type: ignore
        updated_model = await old_model.update(**new_model.__dict__).apply()
        return updated_model._instance
