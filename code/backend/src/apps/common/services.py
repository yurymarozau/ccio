from abc import ABC, abstractmethod
from typing import Type

from apps.common.models import AbstractBaseModel


class BaseModelService(ABC):
    @property
    @abstractmethod
    def model(self) -> Type[AbstractBaseModel]:
        pass
