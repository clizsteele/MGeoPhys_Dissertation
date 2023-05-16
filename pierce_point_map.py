#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:05:15 2023

@author: clizsteele
"""
# Chloe Steele, 28th February 2023, debugging done by Jamie Ward
# This code plots a map of pierce points at the CMB using just the station and event locations. These points are hence
# imaged locations based on the PKP raypaths predicted by PREM.
# import modules
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy
# read in files containing pierce point coordinates
file = np.loadtxt("cmb_bouncepoint_to_plot_2013_2014.txt", dtype=float, delimiter=" ")[1:].astype(str)
source_file = np.loadtxt("cmb_bouncepoint_to_plot_2013_2014_source_side.txt", dtype=float, delimiter=" ")[1:].astype(str)
# read in files
evla = file[:,0].astype(float)
evlo = file[:,1].astype(float)
stla = file[:,2].astype(float)
stlo = file[:,3].astype(float)
evdp = file[:,4].astype(float)
cmb_lat = file[:,5].astype(float)
cmb_lon = file[:,6].astype(float)

cmb_source_lat = source_file[:,5].astype(float)
cmb_source_lon = source_file[:,6].astype(float)


# Plot map
fig = plt.figure(figsize=(30,15))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.set_global()
# Plot data
event = ax.scatter(evlo, evla, color= 'red', marker='*', linewidth=1.5, transform=ccrs.PlateCarree())
cmb = ax.scatter(cmb_lon, cmb_lat, color= 'green', marker='o', linewidth=0.1, alpha=0.1, transform=ccrs.PlateCarree())
cmb_source = ax.scatter(cmb_source_lon, cmb_source_lat, color='blue', marker='o', linewidth=0.1, alpha=0.1, transform=ccrs.PlateCarree())
station = ax.scatter(stlo, stla, color= 'black', marker='^', linewidth=1, transform=ccrs.PlateCarree())

# Plot title
plt.title('Map of event & station locations with associated source & receiver pierce points for the 2013-2014 dataset', fontsize=24)
#gridlines = ax.gridlines(draw_labels=True)
# Plot gridlines
gridliner = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gridliner.xlabels_bottom = True
gridliner.ylabels_left = True
gridliner.xlabels_top = False
gridliner.ylabels_right = False
# Plot legend
ax.legend([event, station, cmb, cmb_source], ['Event location', 'Station location', 'CMB receiver-side pierce points', 'CMB source-side pierce points'], fontsize=18)

# Save figure
#plt.savefig('cmb_pierce_point_map_2013_2014.pdf')
plt.savefig('cmb_pierce_point_map_2013_2014.png')
plt.show()
