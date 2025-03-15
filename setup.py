from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:  
    with open(file_path) as file:
        # Filter out empty lines and lines starting with '-e'
        return [line.strip() for line in file if line.strip() and not line.startswith("-e")]

setup(
    name="fault_detection",  # Changed from "Fault detection" to "fault_detection"
    version="0.0.1",
    author="Amit Negi",
    author_email="negia2091@gmail.com",
    install_requires=get_requirements("requirements.txt"),  
    packages=find_packages(),
)