
class SealedBottle:
    def __init__(self, seal_method: str, **kwargs):
        super().__init__(**kwargs)
        self._seal_method = seal_method
    def open_bottle(self):

        print(f"Open for {self._seal_method}")
    def freezing(self):
        print("Freze before serving maybe")
        
class UnSealedContainer:
    def __init__(self, **kwargs):
        """
        Definition for __init__
        """
        super().__init__(**kwargs)
        pass
    def open_bottle(self):
        print("Ready to serve")
    def heating(self):
        print("Heating coffee maybe")

class Drink(UnSealedContainer, SealedBottle):
    def __init__(self, seal_method: str|None = None):
        super().__init__(seal_method=seal_method)
        self._sealed = bool(seal_method)
    
    def open_bottle(self):
        if self._sealed:
            SealedBottle.open_bottle(self)
        else:
            UnSealedContainer.open_bottle(self)

if __name__ == "__main__":
    drink1 = Drink()
    drink1.open_bottle()
    drink1.heating()
    drink2 = Drink(seal_method='Capped Bottle')
    drink2.open_bottle()
    drink2.freezing()