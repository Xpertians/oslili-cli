from setuptools import setup, find_packages

setup(
    name="oslili-cli", version="0.1",
    description="oslili-cli",
    author="Oscar Valenzuela",
    author_email="oscar.valenzuela.b@gmail.com",
    packages=['src'],
    entry_points={"console_scripts": ["oslili-cli=src.cli:main"]},
    install_requires=["oslili", ],
    url='https://opensourcelicensecompliance.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
)
