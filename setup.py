from setuptools import setup, find_packages
from typing import List
def packageinstaller(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
setup(
    name='mlproject',
    version='0.0.1',
    author='waqas',
    author_email='waqasliaqat630@gmail.com',
    packages=find_packages(),
    install_requires=packageinstaller('requirements.txt')
)