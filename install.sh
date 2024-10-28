#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installing the new(est) sphinx-grasple package"

cd sphinx-grasple
python3 setup.py install
cd ..
rm -rf sphinx-grasple

echo "sphinx-grasple package was installed!"
echo "Ready!"
