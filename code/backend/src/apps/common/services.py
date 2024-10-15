from abc import ABC, abstractmethod
from typing import Type

from apps.common.models import AbstractBaseModel


class BaseModelService(ABC):
    def __init__(self, instance: AbstractBaseModel):
        self._instance = instance

    @property
    @abstractmethod
    def model(self) -> Type[AbstractBaseModel]:
        pass

    @property
    def instance(self) -> AbstractBaseModel:
        return self._instance
