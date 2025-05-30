#!/usr/bin/bash

FILE=$1
LENGTH=$2

AMOUNT=$(grep -F "[$LENGTH]" $FILE | wc -l)
REAL_AMOUNT=$((AMOUNT/2)) # All entries are duplicated

echo "There are $REAL_AMOUNT paths of length $LENGTH between regions."