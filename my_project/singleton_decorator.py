def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        return instances[cls]
    return wrapper

@singleton
class SealedBottle:
    def __init__(self, seal_method: str|None, **kwargs):
        super().__init__(**kwargs)
        self._seal_method = seal_method

    def open_bottle(self):
        print(f"Open for {self._seal_method}")

    def freezing(self):
        print("Freze before serving maybe")

    def get_seal_method(self):
        return self._seal_method

        
if __name__ == "__main__":
    bottle1 = SealedBottle(seal_method="Capped bottle1")
    bottle1.open_bottle()
    print(bottle1.get_seal_method())

    bottle2 = SealedBottle(seal_method="Capped bottle2")

    bottle2.open_bottle()
    print(bottle2.get_seal_method())

    bottle1.open_bottle()
    print(bottle1.get_seal_method())

    print(bottle1 is bottle2)