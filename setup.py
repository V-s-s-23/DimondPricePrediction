from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        return requirements

setup(
    name = "Dimond_Price_Prediction",
    version= "0.0.3",
    author= "Vinay",
    author_email= "civilguy001@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages= find_packages()
)