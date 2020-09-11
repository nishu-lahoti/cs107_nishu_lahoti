#!/bin/bash
# Coder: Katrina
# Sharer: Scarlett
# Listener: Nishu

for x in $(ls);
do
    if [ -x $x ];
    then echo $x
    fi
done

