class Singleton(type):
    _inst = {}
    def __call__(cls, *args, **kargs):
        if cls not in cls._inst:
            instance = super().__call__(*args, **kargs)
            cls._inst[cls] = instance
        return cls._inst[cls]
    
class SealBottle(metaclass=Singleton):
    def __init__(self, name: str):
        print(name)

if __name__ == "__main__":
    a = SealBottle('A cup')
    b = SealBottle('A vase')
    print(a)
    print(b)
    print(a is b)

