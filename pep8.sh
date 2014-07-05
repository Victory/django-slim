#!/bin/sh

find slim/ -iname "*py" | grep -v "migrations" | xargs pep8
RESULT=$?

exit $RESULT