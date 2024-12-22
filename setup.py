from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="Fusion-State-Machine",
    version="0.1.3",
    description="Utility to turn your class into a state machine",
    long_description=long_description,
    long_description_content_type='text/markdown'
    url="https://github.com/Jisus17/Fusion-State-Machine",
    author="Original Author Dhruv Agarwal forked by Jisus17",
    author_email="dhruv.agarwal@shuttl.com",
    license="MIT",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3.7"],
    install_requires=[],
    extras_require={
        "test": ["pytest"],
    },
)
