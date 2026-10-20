#!/bin/sh
# Arm: compare-b-prose-spec. Copies only what this arm is given (workspace/) into the case workspace.
set -e
cp -RL "$(dirname "$0")/workspace/." .
