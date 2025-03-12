from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:  # Correct type hinting
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Correct newline removal
    
    if HYPEN_E_DOT in requirements:  # Correct indentation
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Fault detection",
    version="0.0.1",
    author="Amit Negi",
    author_email="negia2091@gmail.com",
    install_requires=get_requirements("requirements.txt"),  # Correct argument
    packages=find_packages(),  # Correct function call
)
