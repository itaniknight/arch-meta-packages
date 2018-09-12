#!/bin/sh

for item in packages/*/
do
    cd $item
    makepkg -cCr
    cd ../../
done
