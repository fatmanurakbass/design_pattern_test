from abc import ABC, abstractmethod

class PhoneAbstractFactory(ABC):
    @abstractmethod
    def getPhone(self):
        pass