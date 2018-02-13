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
    version="0.0.4",
    author="Deception Logic, Inc.",
    author_email="info@deceptionlogic.com",
    description=("A python wrapper and CLI for the Deception Logic API - "
                 "https://deceptionlogic.com"),
    license="MIT",
    keywords="wrapper library deception logic api cli",
    url="https://github.com/deceptionlogic/deception-api",
    download_url="https://github.com/deceptionlogic/deception-api",
    packages=['deceptionlogic', 'deceptionlogic.aws'],
    long_description=LONG_DESC,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['future', 'requests', 'boto3'],
    script=['deceptionlogic/bin/deception']
)
