from miphone import MiPhone
from iphone import iPhone

class PhoneFactory():

    def getPhone(self, phone):
        if phone.lower() == "miphone":
            return MiPhone()
        if phone.lower() == "iphone":
            return iPhone()
        else:
            return None