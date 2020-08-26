#!/bin/bash

echo "[LOG] Setting up project"
cd ~/zips
unzip $(ls -t | head -n1) ~/isteam

echo "[LOG] Cleaning up the directory"
cd ~/isteam
rm -r ./*

echo "[LOG] Setting up python env"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "[LOG] Build CSS"
npm i
npm bundle

