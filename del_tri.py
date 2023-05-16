#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:10:13 2023

@author: clizsteele
This code is to be run after sub_direc.py and deletes all the sub-array directories that contain less than 10 SAC files
"""
#import modules
import obspy
import os
import os.path
import numpy as np
import glob as glob


#paths to directories and files
folder_path = 'trial_2013*/processed/'
folder_paths = 'processed/'

paths = glob.glob('/nfs/a301/ee19ces/diss_data_2004_2006/trial_2013*')

x = 'nfs/a301/ee19ces/diss_data_2004_2006/trial_2013*/processed'
path = '/nfs/a301/ee19ces/diss_data_2004_2006/'
#print(paths)

for path in paths:
    folder = path + '/' + folder_paths
    print('These are folder:', folder)
    good_event = True
    #Defining extremes to make regular grid of centre points of sub-arrays
    lon_max = -60
    lon_min = -125
    lat_min = 25
    lat_max = 50
    stepsize = 5

           
            #Defining centre points of sub arrays
    for x in range(lon_min, lon_max, stepsize):
        for y in range(lat_min, lat_max, stepsize):
            var = x, y
            print(var)
            a = str(var[0])
            b = str(var[1])
           
            with open(folder + 'sub_arrays_'+ a +'_'+ b +'_.txt', 'r') as file:
                file.readlines()
                count = 0
                file.seek(0)
                for line in enumerate(file):
                    if line != "\n":
                        count += 1
                        print('here')
   
                if count <= 10:
                    print(folder)
                    print('Deleting sub_arrays_'+ a +'_'+ b +'_.txt')
                    os.remove(folder + '/' 'sub_arrays_'+ a +'_'+ b +'_.txt')
                    #file.close()
   
                else:
                    pass
