#!/bin/sh
# Arm: map and skill. Copies the fixture's map (never its code) and the brief into the case workspace.
set -e
cp -RL "$(dirname "$0")/fixture/." .
rm -rf src tests
cp -RL "$(dirname "$0")/workspace/." .
