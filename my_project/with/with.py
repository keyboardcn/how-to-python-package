from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    with open('sample.txt', 'r') as f:
        yield f.readlines()
    print("Exiting the context")
    
if __name__ == "__main__":
    with my_context_manager() as file_data:
        print("Inside the context")
        for l in file_data:
            print('line: ', l.strip())
    print("Outside the context")