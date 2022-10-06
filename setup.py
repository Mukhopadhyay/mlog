"""The setup script."""

from monolg import *
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as req:
    requirements = req.split()

with open("requirements_dev.txt") as req:
    dev_requirements = req.split()

setup(
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Centralized logging for Python using MongoDB",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="monolg",
    name="monolg",
    packages=find_packages(include=["monolg", "monolg.*"]),
    test_suite="tests",
    tests_require=dev_requirements,
    url="https://github.com/Mukhopadhyay/monolg",
    version="0.0.1",
    zip_safe=False,
)
