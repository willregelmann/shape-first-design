#!/bin/sh
# Arm: compare-a-brief-only. Copies only what this arm is given (workspace/) into the case workspace.
set -e
cp -RL "$(dirname "$0")/workspace/." .
