#!/usr/bin/env bash
"""
Shell script that runs the Bootstrap_Peak_Recover_XY.py (https://github.com/eejwa/Array_Seis_Circle/blob/master/scripts/Bootstrap_Peak_Recover_XY.py)
and Clustering.py (https://github.com/eejwa/Array_Seis_Circle/blob/master/scripts/Clustering.py) to produce slowness-back azimuth grids for each sub-array of each event.
Shell script written by Chloe Steele, corrections made by Jamie Ward.
"""
cwd=$(pwd)

for d in 20140518*
do
  echo $d
  cd ${d}/processed/
  cwd_dir=$(pwd)
  for file in sub_array*/
  do
    cd $file
    echo $file
    pwd
    Bootstrap_Peak_Recover_XY.py
    echo "Done_bootstrap"
    Clustering.py
    echo "Done_clustering"
    cd $cwd_dir
    pwd
  done
  cd $cwd_dir
done
