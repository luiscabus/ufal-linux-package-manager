#!/bin/sh

cd ~/.mpu/packages

bzip2 -d *.tbz2

for tarball in *.tar ; do
    tar -xf "$tarball"
done

rm *.tar
