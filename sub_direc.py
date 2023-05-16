#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:47:57 2023

@author: clizsteele
This code reads the locational information from SAC files, writes a list of SAC files that fit within a certain 6x6 degree sub-array
across the continental USA and writes a list of these SAC files to a txt file.
"""

#import modules
import obspy
import os
import os.path
import numpy as np
import glob as glob


#paths to directories and files
folder_path = 'trial_2013*/processed'
folder_paths = 'processed/'

paths = glob.glob('/nfs/a301/ee19ces/diss_data_2004_2006/trial_2013*')

x = 'nfs/a301/ee19ces/diss_data_2004_2006/trial_2013*/processed'
path = '/nfs/a301/ee19ces/diss_data_2004_2006/'

# Move into the processed folder of an event
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
   
    #Count number of SAC files within the folder
    count = 0
    #print('Help')
       
    #counting SAC files -> to see if the event is useful, count = no. of stations
    for path in os.listdir(folder):
        #if os.path.isfile(os.path.join(folder, path)):
            count += 1
            #print(count)
            #print('File count:', count)
    #looping through directories to see if sufficient station numbers
    for i in folder_path:
        if count <= 20:
            print('Folder count:', count)
            print('Count <30, ignore event')
            #os.chdir(path)
            good_event = False
            break
        elif count == 0:
            print('No events')
            good_event = False
            break
        elif count > 20:
            print('Good event!')
# read files    
    filenames = glob.glob(folder + '/*.SAC')
    # Obtain header information from SAC files
    for j in range(len(filenames)):
        #print(filenames)
        st = obspy.read(filenames[j])[0]
        print(st)
       
        lat = st.stats.sac.stla #station latitude data
        lon = st.stats.sac.stlo #station longitude data
        baz = st.stats.sac.baz #back az data
        dist = st.stats.sac.gcarc #distance data
        print('Read SAC files')

               
                #Defining centre points of sub arrays
        for x in range(lon_min, lon_max, stepsize):
            for y in range(lat_min, lat_max, stepsize):
                var = x, y
                print(var)
                a = str(var[0])
                b = str(var[1])
                # Create txt file of a list of SAC files within a sub-array
                with open(folder + 'sub_arrays_'+ a +'_'+ b +'_.txt', 'a') as file:
                    box_lat_min = var[1]-2
                    box_lat_max = var[1]+2
                    box_lon_min = var[0]-2
                    box_lon_max = var[0]+2
   
                    if lat <= box_lat_max and lat >= box_lat_min and lon <= box_lon_max and lon >= box_lon_min:
                        print('Filenames:', filenames[j])
                        file.write(filenames[j])
                        file.write('\n')
                        print('Written to file!')
                             
                    else:
                        pass
                        #print('Pass')
