import time
import random
from typing import Literal
from functools import wraps
from pydantic import BaseModel
class CircuitState(BaseModel):
    state: Literal['CLOSED', 'HALF_OPEN', 'OPEN']
    failures: int
    last_failure_time: float | None

class CircuitBreaker:
    cls_threshold = 3
    cls_timeout = 3  # in seconds
    cls_tracker: dict[str, CircuitState] = {}
    _inst = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._inst:
            instance = super().__new__(cls)
            cls._inst[cls] = instance
        return cls._inst[cls]
    
    '''
    important! def __call__ can be used only when we create an instance of the class
    '''
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func.__name__ not in self.cls_tracker:
                self.cls_tracker[func.__name__] = CircuitState(state='CLOSED', failures=0, last_failure_time=None)
            tracker = self.cls_tracker[func.__name__]

            if tracker.state == 'OPEN':
                if time.time() - tracker.last_failure_time > self.cls_timeout:
                    tracker.state = 'HALF_OPEN'
                else:
                    raise Exception(f"{func.__name__}Circuit is OPEN. ${tracker.failures} Call failed.")
            try:
                result = func(*args, **kwargs)
                tracker.failures = 0
                if tracker.state == 'HALF_OPEN':
                    tracker.state = 'CLOSED'
                return result
            except Exception as e:
                tracker.failures += 1
                tracker.last_failure_time = time.time()
                if tracker.failures >= self.cls_threshold:
                    tracker.state = 'OPEN'
                raise e
        return wrapper
    
@CircuitBreaker()
def unstable_function() -> int:
    if random.random() < 0.3:
        time.sleep(1)
        return 100
    else:
        raise ValueError("Unstable function failed!")
    
if __name__ == "__main__":
    breaker1 = CircuitBreaker()
    breaker2 = CircuitBreaker()
    print(breaker1 is breaker2)  # Should print True, confirming singleton behavior
    for i in range(20):
        try:
            print(unstable_function())
        except Exception as e:
            print(e)