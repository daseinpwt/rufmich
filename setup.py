import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="callmex",
    version="0.0.7",
    author="daseinpwt",
    author_email="daseinpwt@gmail.com",
    description="A Python server implementaion for JSON-RPC 2.0 over HTTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daseinpwt/callme",
    packages=setuptools.find_packages(),
    install_requires=[
        'flask',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)