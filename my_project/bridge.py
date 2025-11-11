
class SealedBottle:
    def __init__(self, seal_method: str):
        self._seal_method = seal_method
    def open_bottle(self):
        print(f"Open for {self._seal_method}")
class UnSealedContainer:
    def __init__(self):
        """
        Definition for __init__
        """
        pass
    def open_bottle(self):
        print("Ready to serve")

class Drink:
    def __init__(self, seal_method: str|None = None):
        if seal_method:
            self._impl = SealedBottle(seal_method)
        else:
            self._impl = UnSealedContainer()

    def open_bottle(self):
        self._impl.open_bottle()

if __name__ == "__main__":
    drink1 = Drink()
    drink1.open_bottle()
    drink2 = Drink('Capped Bottle')
    drink2.open_bottle()