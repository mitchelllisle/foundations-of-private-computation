#!/usr/bin/env sh
set -e

cd /source
pip install -U pip
make install-all
make install
make test