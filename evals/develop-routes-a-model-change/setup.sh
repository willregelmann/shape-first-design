#!/bin/sh
# Copies the fixture project into the case's workspace (the current directory).
set -e
cp -RL "$(dirname "$0")/fixture/." .
