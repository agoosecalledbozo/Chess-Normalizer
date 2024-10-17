#setup.py
from setuptools import setup, find_packages

setup(
    name="chessNormalizer",
    version="0.1.0",
    description="A chess move normalization library for Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kayden",
    author_email="none",
    url="none",
    packages=find_packages(),
    install_requires=["python-chess>=0.31.4"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
