#!/usr/bin/env sh
set -e

cd /source
make install-all
make test
