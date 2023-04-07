#!/bin/bash
rm -rf dist/*
rm -rf build/
rm -rf oslili_cli.egg-info/
python3 setup.py sdist bdist_wheel
