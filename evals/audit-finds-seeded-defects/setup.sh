#!/bin/sh
# Copies the fixture project into the case's workspace (the current directory),
# then replaces its code and tests with a drifted version (seeded/) that has
# known defects: the audit has to find them.
set -e
cp -RL "$(dirname "$0")/fixture/." .
rm -rf src tests
cp -R "$(dirname "$0")/seeded/." .
