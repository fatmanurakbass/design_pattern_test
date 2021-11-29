from phone_factory import PhoneFactory

class Demo():
        factory = PhoneFactory()
        miphone = factory.getPhone("MiPhone")
        iphone = factory.getPhone("iPhone")

if __name__ == "__main__":
    Demo()