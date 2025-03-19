from setuptools import find_packages,setup
from typing import List



def get_requirement()->List[str]:
    ''''

    this  function wii retrun a list
    '''
    requirement_list=[]
    try:
        with open('requirements.txt','r') as file:
             ##Readlines from the files
             lines=file.readlines()
        for line in lines:
             ##process each lines
            requirement=line.strip()
            ##ignore the empty lines and -e .
            if requirement and requirement != '-e .':
                requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    
    return requirement_list
print(get_requirement())

setup(
name='mlproject',
version='0.0.1',
author='yeri',
author_email='adedejiakiwale@gmail.com',
packages=find_packages(),
install_requires=get_requirement()
)




       








