#!/bin/bash

if [ ! -e public/.git ]; then
  rm -rf public
  git clone -b publish git@github.com:kaist-s4/kaist-s4.github.io.git public
fi

hugo

cd public
git add .
git commit -m "$(date)"
git push
