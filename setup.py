"""
DeceptionLogicAPI setup
"""
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    long_desc = f.read()

setup(
    name="DeceptionLogicAPI",
    version="0.0.1",
    author="Deception Logic, Corp.",
    author_email="info@deceptionlogic.com",
    description=("A python wrapper for the Deception Logic API - "
                 "https://deceptionlogic.com"),
    license="MIT",
    keywords="wrapper library deception logic api",
    url="https://github.com/deceptionlogic/deception-api",
    download_url="https://github.com/deceptionlogic/deception-api",
    packages=['DeceptionLogicAPI'],
    long_description=long_desc,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['requests']
)
