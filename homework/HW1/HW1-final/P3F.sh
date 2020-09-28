#!/bin/bash

for x in $(ls);
do
    if [ -f $x ];
    then echo -n $x && cat $x | wc -l  
    fi
done
