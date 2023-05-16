#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:46:02 2023

@author: clizsteele
This code extracts the station and event latitudes and longitudes, and writes these parameters to map_pierce_general.txt
Chloe Steele, 2023
"""
# import modules
import glob
import obspy
import os

#file paths
paths = glob.glob('/nfs/a301/ee19ces/diss_data_2004_2006/20130406*')
folder_paths = 'processed/'

# go into correct directory, read the SAC files, write stla, stlo, evla, evdp to txt file
for path in paths:
    folder = path + '/' + folder_paths
    filenames = glob.glob(folder + '/*.SAC')
    print('A', path)
    st = obspy.read(folder + '/*.SAC')
    print(st)
    with open('map_pierce_general_2013_2014.txt', 'a') as file:
        for tr in st:
            stla = tr.stats.sac.stla
            stlo = tr.stats.sac.stlo
            evla = tr.stats.sac.evla
            evlo = tr.stats.sac.evlo
            evdp = tr.stats.sac.evdp
            print(evdp)
            #file.write(f"{stla} {stlo} {evla} {evlo} {evdp} /n")
