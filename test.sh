#!/usr/bin/env bash
# Exit on first error
set -e

# Run our linter
flake8 .

# Run our tests
nosetests --nocapture $* email_split/test/*.py
