"""
deceptionlogic setup
"""
import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.rst')) as f:
    LONG_DESC = f.read()

setup(
    name="deceptionlogic",
    version="0.0.1",
    author="Deception Logic, Corp.",
    author_email="info@deceptionlogic.com",
    description=("A python wrapper for the Deception Logic API - "
                 "https://deceptionlogic.com"),
    license="MIT",
    keywords="wrapper library deception logic api",
    url="https://github.com/deceptionlogic/deception-api",
    download_url="https://github.com/deceptionlogic/deception-api",
    packages=['deceptionlogic'],
    long_description=LONG_DESC,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['requests']
)
