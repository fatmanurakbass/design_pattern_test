from phone_abstract_factory import PhoneAbstractFactory
from miphone import MiPhone

class XiaoMiFactory(PhoneAbstractFactory):

    def getPhone(self):
            return MiPhone()
