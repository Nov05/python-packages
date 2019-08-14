import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-nov05",
    version="0.0.6",
    author="nov05",
    author_email="arwen_liu@hotmail.com",
    description="DS5 Unit3 example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nov05/python-packages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)