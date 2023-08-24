#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installing the new sphinx-grasple package"

git clone https://github.com/dbalague/sphinx-grasple

cd sphinx-grasple
python3 setup.py install
cd ..
rm -rf sphinx-grasple

echo "sphinx-grasple package was installed!"
echo "Ready!"
