#!/bin/bash
cat apollo13.txt | grep -c [0-9]
grep --help | grep "\-c,"
find . -type f | grep "\.py" | wc -l
find . -type f -perm 001 | wc -l
find . -type f,d -perm 001 | wc -l
