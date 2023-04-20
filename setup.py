from setuptools import setup, find_packages

setup(
    name="oslili-cli", version="0.3",
    description="Open Source License Identification Library",
    author="Oscar Valenzuela",
    author_email="oscar.valenzuela.b@gmail.com",
    packages=['src'],
    entry_points={"console_scripts": ["oslili-cli=src.cli:main"]},
    install_requires=["oslili", ],
    url='https://opensourcelicensecompliance.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License'
    ],
)
