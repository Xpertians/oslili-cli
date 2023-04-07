#!/bin/bash
rm -rf dist/*
rm -rf build/
python3 setup.py sdist bdist_wheel
#pip3 uninstall kotaix  -y  >> logs/install-pip.log
#pip3 install dist/kotaix-*.whl >> logs/install-pip.log
