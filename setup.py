from setuptools import setup

requirements = [line for line in open('requirements.txt')]

setup(
    name='sam',
    version='1.0',
    description="Personal modules for Sam's use",
    author="Sam Cunliffe",
    url="https://github.com/samcunliffe/sam",
    packages=['sam', 'sam.pp'],
    package_dir={
        'sam': 'sam/sam',
        'sam.pp': 'sam/sam/pp'
    },
    install_requires = requirements,
)
