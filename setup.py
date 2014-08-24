import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SwampDragon-fileupload",
    version="0.1.2",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("File upload handler for SwampDragon"),
    license="BSD",
    keywords="SwampDragon, file upload",
    url="https://github.com/jonashagstedt/swampdragon-fileupload",
    packages=find_packages(),
    long_description=read('README.md'),
    include_package_data=True,
    install_requires=[
        "SwampDragon"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
