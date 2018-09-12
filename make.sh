#!/bin/sh

currdir=$(pwd)
echo $currdir
cd ~/public/meta-packages/packages/$1 && makepkg -cCfirs
cd $currdir
