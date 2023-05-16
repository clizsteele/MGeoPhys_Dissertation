#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:26:02 2023

@author: clizsteele
Creates a map showing the centre points of the sub-arrays across the continental USA.
"""
# import modules
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy


#set limits of sub-array
lon_max = -60
lon_min = -125
lat_min = 25
lat_max = 50
stepsize = 3

# Plot figures
fig = plt.figure(figsize=(30,15))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.set_global()
# Set extent
ax.set_extent([-180, -50, 0, 90], crs=ccrs.PlateCarree())
plt.title('Centre points of sub-arrays', fontsize=32)

# Set grid lines
gridliner = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gridliner.xlabels_bottom = True
gridliner.ylabels_left = True
gridliner.xlabels_top = False
gridliner.ylabels_right = False

# Calculating and plotting the centres of the sub-arrays
for x in range(lon_min, lon_max, stepsize):
    for y in range(lat_min, lat_max, stepsize):
        var = x, y
        #print(var)
        a = str(var[0])
        b = str(var[1])
        c = ax.scatter(a, b, color='red')
 # Plot legend      
ax.legend([c], ['Centre of sub-arrays'], fontsize=18)

#plt.savefig('sub_array_centres.pdf')
plt.savefig('sub_array_centres.png')
plt.show()
