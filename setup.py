from setuptools import setup, find_packages

setup(
    name="chessNormalizer",
    use_scm_version=True,
    description="A chess move normalization library for Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kayden",
    author_email="btskt613@gmail.com",
    url="https://github.com/agoosecalledbozo/Chess-Normalizer",
    packages=find_packages(),
    install_requires=["python-chess>=0.31.4"],
    setup_requires=["setuptools_scm"],  # Required to use setuptools_scm
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
