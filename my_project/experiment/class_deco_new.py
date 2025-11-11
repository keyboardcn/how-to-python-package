from functools import wraps
class DemoDecorator:
    def __new__(cls, func):
        print("Before calling the function.")
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    
@DemoDecorator
def my_function(k: int) -> str:
    '''
    a simple function to demonstrate decorator
    '''
    print(f"**Inside the function.{k}")
    return "Function Result"

if __name__ == "__main__":
    my_function(5)
    print(my_function.__name__)
    print(my_function.__doc__)