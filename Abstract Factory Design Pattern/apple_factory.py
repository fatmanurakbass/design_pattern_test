from phone_abstract_factory import PhoneAbstractFactory
from iphone import iPhone

class AppleFactory(PhoneAbstractFactory):

    def getPhone(self):
            return iPhone()
