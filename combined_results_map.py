#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:41:01 2023

@author: ee19ces
"""
# Chloe Steele, 14/04/2023. Plotting pierce points at the CMB for data collected for 2013-2014 dataset.

# import modules
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy
import matplotlib.ticker as xticks

# Load data
file = np.loadtxt("Final_results.csv", dtype=float, delimiter=" ")[1:].astype(str)
files = np.loadtxt("Final_results_stations.csv", dtype=float, delimiter=" ")[1:].astype(str)
f = np.loadtxt("PKIKP_pierce_points.csv", dtype=float, delimiter=" ")[1:].astype(str)

# Read in the data by column
slowness = file[:,0].astype(float)
baz = file[:,1].astype(float)
sta_lat_mean = file[:,2].astype(float)
sta_lon_mean = file[:,3].astype(float)
BC_lat_rec = file[:,4].astype(float)
BC_lon_rec = file[:,5].astype(float)
BC_lat_sou = file[:,6].astype(float)
BC_lon_sou = file[:,7].astype(float)
AB_lat_rec = file[:,8].astype(float)
AB_lon_rec = file[:,9].astype(float)
AB_lat_sou = file[:,10].astype(float)
AB_lon_sou = file[:,11].astype(float)
slow_std = file[:,12].astype(float)
baz_std = file[:,13].astype(float)
evla = files[:,0].astype(float)
evlo = files[:,1].astype(float)

rec_lat = f[:,4].astype(float)
rec_lon = f[:,5].astype(float)
sou_lat = f[:,6].astype(float)
sou_lon = f[:,7].astype(float)

# Plot map
fig = plt.figure(figsize=(16,8))

ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

ax.coastlines()
ax.gridlines()
ax.set_global()
plt.title('Map of scattering regions for both source & receiver side scattering at the CMB using PKP & PKIKP', fontsize=18)

#Plotting Pierce points. These should be named the other way, i.e. BC_rec is actually BC_sou
BC_rec = ax.scatter(BC_lon_rec, BC_lat_rec, color= 'blue', marker='s', linewidth=1, transform=ccrs.PlateCarree())
BC_sou = ax.scatter(BC_lon_sou, BC_lat_sou, color= 'cyan', marker='s', linewidth=1, transform=ccrs.PlateCarree())
AB_rec = ax.scatter(AB_lon_rec, AB_lat_rec, color= 'red', marker='s', linewidth=1, transform=ccrs.PlateCarree())
AB_sou = ax.scatter(AB_lon_sou, AB_lat_sou, color= 'magenta', marker='s', linewidth=1, transform=ccrs.PlateCarree())
PKIKP_rec = ax.scatter(rec_lon, rec_lat, color='yellow', marker='s', linewidth=2, transform=ccrs.PlateCarree())
PKIKP_sou = ax.scatter(sou_lon, sou_lat, color='black', marker='s', linewidth=2, transform=ccrs.PlateCarree())
stations = ax.scatter(sta_lon_mean, sta_lat_mean, color= 'green', marker='^', linewidth=1, transform=ccrs.PlateCarree())
event = ax.scatter(evlo, evla, color= 'black', marker='*', linewidth=2, transform=ccrs.PlateCarree())
# Plot legend
ax.legend([AB_rec, AB_sou, BC_rec, BC_sou, PKIKP_rec, PKIKP_sou, stations, event], ['AB Source side scattering', 'AB Receiver side scattering', 'BC Source side scattering', 'BC Receiver side scattering', 'PKIKP Source side scattering', 'PKIKP Receiver side scattering', 'Mean station location', 'Earthquake epicentre'], fontsize=12)
#Plot grid lines
gridliner = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gridliner.xlabels_bottom = True
gridliner.ylabels_left = True
gridliner.xlabels_top = False
gridliner.ylabels_right = False

plt.savefig('Final_results_map_PKP_PKIKP.png')
