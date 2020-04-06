import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="aioprint",
    version="0.0.2",
    description="An inherently useless Python library so you can log things without blocking your async program at all.",
    url="https://github.com/crrapi/aioprint",
    author="Chris Rrapi",
    author_email="toadawes12@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
