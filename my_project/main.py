# my_project/main.py

# Import the function from your installed package
from hello_package.greeter import say_hello

def run_my_app():
    """
    This is the main function of your application that uses the hello_package.
    """
    print("--- Starting My Application ---")

    # Call the function from the imported package
    say_hello()

    print("--- Application Finished ---")

if __name__ == "__main__":
    run_my_app()
