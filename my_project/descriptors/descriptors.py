from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        print(f"Setting {name} for {owner}")
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        print("Getting", getattr(obj, self.private_name))
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, value):
        print(f"Setting {self.private_name} to {value}")
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class OneOf(Validator):
    def __init__(self, *options):
        self.options = options

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Value {value} not in options {self.options}")

class Component:
    kind = OneOf("small", "medium", "large")

    def __init__(self, kind):
        self.kind = kind

if __name__ == "__main__":
    c= Component("medium")
    print(c.kind)
    b = Component("large")
    print(b.kind)