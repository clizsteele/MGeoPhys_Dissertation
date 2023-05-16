#!/usr/bin/env bash
"""
Bash code that reads the txt files created by sub_direc.py and creates directories containing a copy of the SAC files.
Chloe Steele, 2023
"""

cwd=$(pwd)

for d in 2012*
do
  cd ${d}/processed/

  for file in sub_array*
  do
    mkdir "${file%.*}"
    echo "$file"
   
    while read -r line; do
      echo -e "$line"
    cp $line "${file%.*}"
    done <$file

  done
  cd $cwd
done
