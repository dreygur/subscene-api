import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="subscene-api2",
    version="0.0.1",
    author="Rakibul Yeasin",
    author_email="ryeasin03@gmail.com",
    description="A Python wrapper for SubScene",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dreygur/subscene-api",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)