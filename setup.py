# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypublibike',
    version='3.0.1',
    description='A python wrapper around the PubliBike API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/eliabieri/pypublibike',
    author='Elia Bieri',
    author_email='bieri.elia@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires='>=3.7',
    install_requires=['requests', 'haversine'],
)
