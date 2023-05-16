#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:11:39 2023

@author: ee19ces
"""
# Chloe Steele, 30/03/2023
# Go into the output results folder from the DBSCAN algorithm, and extract the
# directivity information and errors of the scattering events
import obspy
import os
import os.path
import numpy as np
import glob as glob


#paths to directories and files
folder_path = 'sub_array_-*_*_/Results'
folder_paths = 'Results/'

paths = glob.glob('/nfs/a301/ee19ces/diss_data_2004_2006/20140518*/processed/sub_array*')
#x = 'nfs/a301/ee19ces/diss_data_2004_2006/20130525/processed/sub_array*/Results'
path = '/nfs/a301/ee19ces/diss_data_2004_2006/20140518*/processed/'
new = []

for path in paths:
    folder = path + '/' + folder_paths
    #print(folder)
    for path in os.listdir(folder):
        os.chdir(folder)
        #print(os.path.isfile("Clustering_Results_0.50_2.00.txt")) #checks if the file exists in all directories
        with open("Clustering_Results_0.50_2.00.txt", 'r') as f:
                a = f.readlines()[1:]
                c = a[0]
                b = str(c)
                slow = b.split(" ")
                slowness = slow[9]
                back_az = slow[13]
                station_mean_lat = slow[6] #mean station latitude
                station_mean_lon = slow[7] #mean station longitude
                baz_diff = slow[14] #difference between predicted and observed back az
                slow_diff = slow[10] #difference between predicted and observed slowness
                baz_std_dev = slow[15] #standard deviation of back az
                slow_std = slow[11] #standard deviation of slowness
                sta_lat = slow[6]
                sta_lon = slow[7]
                test = os.getcwd()
                os.chdir('../..')
               
                print(test)
                print(slowness)
               
# Write good clustered events to file
        with open("clustering2.txt", 'a') as file:
            file.write(slow_diff)
            file.write(' ')
            file.write(baz_diff)
            file.write(' ')
            file.write(station_mean_lat)
            file.write(' ')
            file.write(station_mean_lon)
            file.write('\n')
            file.close()
       
        with open("Errors2.txt", 'a') as filed:
            filed.write(slow_std)
            filed.write(' ')
            filed.write(baz_std_dev)
            filed.write(' ')
            filed.write(station_mean_lat)
            filed.write(' ')
            filed.write(station_mean_lon)
            filed.write('\n')
            filed.close()

        os.chdir(folder)
