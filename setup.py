from distutils.core import setup

import setuptools  # noqa
from Cython.Build import cythonize

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name="aioprint",
    version="0.0.3",
    description="Provides an asynchronous interface for print() using aiofiles.",
    url="https://github.com/crrapi/aioprint",
    author="crrapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    ext_modules=cythonize("aioprint/*.py", compiler_directives={"language_level": "3"}),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
