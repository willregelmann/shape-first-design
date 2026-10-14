#!/bin/sh
# Copies a fixture project into the case's workspace (the current directory).
set -e
cp -R "$(dirname "$0")/chores/." .
