from setuptools import setup, find_packages

setup(
    name='my-package',
    author='Yuri Prezument',
    author_email='y@yprez.com',
    version='0.0.0',
    packages=find_packages(),
    license='ISC',
    url='http://github.com/yprez/',
    description='Sample package',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
    classifiers=(
    ),
)
