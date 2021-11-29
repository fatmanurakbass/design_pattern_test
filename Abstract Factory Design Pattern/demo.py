from xiaomi_factory import XiaoMiFactory
from apple_factory import AppleFactory

class Demo():

        xiaomi_factory = XiaoMiFactory()
        apple_factory = AppleFactory()

        xiaomi_factory.getPhone()
        apple_factory.getPhone()

if __name__ == "__main__":
    Demo()