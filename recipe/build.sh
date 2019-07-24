#!/bin/sh

#BIN=$PREFIX/bin
#mkdir -p $BIN

#cp $SRC_DIR/repo $BIN
cp $SRC_DIR/Makefile $PREFIX

$PYTHON setup.py install
