#!/bin/bash
PLATFORM=linux64
VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
curl http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip | bsdtar -xvf - -C env/bin/
chmod +x ./env/bin/chromedriver
mkdir profile_dir
