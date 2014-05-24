#!/bin/sh

# Used in .git/hooks/pre-commit with the following code snipet
#
# LINT="$(git rev-parse --show-toplevel)/lint-check.sh"
# $LINT
# if [ $? -ne 0 ]; then
#     echo "Not committing do to Lint errors."
#     exit 1
# fi

LINT="pocketlint"
cd "$(git rev-parse --show-toplevel)"
CWD=$(pwd)

JSPATH=$(git status --porcelain | grep ".*js$" | \
    grep -v "^R" | awk '{print $2}')
HTMLPATH=$(git status --porcelain | grep ".*html$" | \
    grep -v "^R" | awk '{print $2}')
CSSPATH=$(git status --porcelain | grep ".*css$" | \
    grep -v "^R" | awk '{print $2}')
PYTHONPATH=$(git status --porcelain | grep ".*py$" | \
    grep -v "^R" | awk '{print $2}')

RESULT=0
if [ ! -z "$JSPATH" ]; then
    echo "js: $JSPATH"
    $LINT  $JSPATH
    RESULT=$(($? + $RESULT))
fi

if [ ! -z "$HTMLPATH" ]; then
    echo "html: $HTMLPATH"
    $LINT  $HTMLPATH
    RESULT=$(($? + $RESULT))
fi

if [ ! -z "$PYTHONPATH" ]; then
    echo "py: $PYTHONPATH"
    $LINT $PYTHONPATH
    RESULT=$(($? + $RESULT))
fi
exit $RESULT
