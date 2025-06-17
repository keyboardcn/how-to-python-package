# hello_package/setup.py

from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='hello_package', # The name of your package
    version='0.1.0',      # The initial version number
    author='Your Name',   # Replace with your name
    author_email='your.email@example.com', # Replace with your email
    description='A simple package that prints "hello".', # Short description
    long_description=open('README.md').read(), # Long description from README.md
    long_description_content_type='text/markdown', # Type of long description
    url='https://github.com/keyboardcn/hello_package', # Replace with your package's URL (e.g., GitHub repo)
    packages=find_packages(), # Automatically find all packages in the current directory
    classifiers=[ # Classifiers help users find your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Example license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', # Minimum Python version required
    # install_requires=[ # List of dependencies required by your package
    #     # 'some_dependency>=1.0', # Example: uncomment and replace with actual dependencies if any
    # ],
    install_requires=read_requirements(), # Read dependencies from requirements.txt
)