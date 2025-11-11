class Subject:
    _observers = []
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        del self._observers[:]
        print("Cleared all observers")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception if any
    
    def register_observer(self, observer):
        self._observers.append(observer)
        print(f"Registered observer: {observer}")
    
    def unregister_observer(self, observer):
        self._observers.remove(observer)
        print(f"Unregistered observer: {observer}")

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"Observer {self.name} received message: {message}")

if __name__ == "__main__":
    with Subject() as subject:
        obs1 = Observer("Observer1")
        obs2 = Observer("Observer2")
        
        subject.register_observer(obs1)
        subject.register_observer(obs2)
        
        subject.notify_observers("Hello Observers!")
        
        subject.unregister_observer(obs1)
        
        subject.notify_observers("Goodbye Observer1!")