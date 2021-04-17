#!/bin/bash

TMPFILE=$(mktemp)
sed 's/(/1 + p /g;s/)/_1 + p /g' 01-input.txt | sed 's/ + p//' | dc > $TMPFILE
tail -n 1 $TMPFILE
nl -v 2 $TMPFILE | grep -- -1$ | head -n 1 | cut -f1 | tr -d ' '


rm -f $TMPFILE

