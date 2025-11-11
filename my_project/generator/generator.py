
class Iterable:
    def __iter__(self):
        self.value = 10
        return self
    
    def __next__(self):
        if self.value > 0:
            current = self.value
            self.value -= 1
            return current
        else:
            raise StopIteration
        
class Generator(metaclass=type):
    def __iter__(self):
        return self.generate()
    
    def generate(self, limit=10):
        while limit > 0:
            yield limit
            limit -= 1

if __name__ == "__main__":
    g = Generator()
    for val in g:
        print('{} - {:2%}'.format('Value', val))