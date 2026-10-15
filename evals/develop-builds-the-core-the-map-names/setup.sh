#!/bin/sh
# Copies the fixture project into the case's workspace (the current directory),
# keeping only its map: the case builds the code from the map alone.
set -e
cp -RL "$(dirname "$0")/fixture/." .
rm -rf src tests
