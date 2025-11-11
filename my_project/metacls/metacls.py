class Human(type):
    def __new__(cls, name: str, bases, cls_dict, **kwargs):
        cls_dict['species'] = 'Homo Sapiens'
        print(f"Mataclass {cls.__name__} is modifying class {name}")
        instance = super().__new__(cls, name, bases, cls_dict)
        if kwargs:
            for k, v in kwargs.items():
                setattr(instance, k, v)
        return instance
    
class Person:
    def __init__(self, name: str):
        print('init Person')
        self.name = name

    def working(self):
        print('Unknown')

class Employee(Person, metaclass=Human, freedom= True, country="USA"):
    def __init__(self, name):
        super().__init__(name)
    def working(self):
        print('Yes')

if __name__ == "__main__":
    p = Employee("John")
    print(Employee.__dict__)
