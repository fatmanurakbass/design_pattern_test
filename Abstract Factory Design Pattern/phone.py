from __future__ import annotations
from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def getPhone(self) -> Phone:
        pass