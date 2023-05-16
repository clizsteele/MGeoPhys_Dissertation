# MGeoPhys_Dissertation
Codes used for a Masters Thesis investigating 'Directivity Information of PKP precursors.' Submitted in accordance with the requirements for the degree MGeoPhys BSc Geophysical Sciences, University of Leeds

preprocessing_codes.py convert mseed files to SAC files and filter them. Provided by Sebastian Rost & Jamie Ward.

plot_data.csh plots the stacked seismograms. Code provided by Sebastian Rost.

sub_direc.py splits SAC files into sub-arrays and creates txt files with a list of SAC files within each sub-arrays.

folders.sh takes the txt files produced by sub_direc.py and makes the sub-array directories and copies the relevant SAC files into the directories.

del_tri.py deletes all the sub-array directories that contain less than 10 SAC files

map_staion_event_pierce.py extracts stla, stlo, evla, evlo and evdp and stores this in map_pierce_general.txt

cmb_bounce.sh takes map_pierce_general.txt and runs it through TauP to produce cmb_lat and cmb_lon, the pierce points at the CMB.

blue_sq_direc.sh allows the DBSCAN algorithm to run through the directory structure created above.
The scripts called within this shell script were written by Jamie Ward and are available at:
https://github.com/eejwa/Array_Seis_Circle/tree/master/scripts

PKP.py goes into the Clustering_Results_0.50_2.00.txt file, extracts directivity information and errors of arrivals that have clustered on PKP on
the slowness-backazimuth grids and writes these to clustering.txt and errors.txt for each event.

PKP_pierce_point_seb.csh takes the directivity information and mean station location of the sub-array and projects the scattering region down to the
CMB assuming the projection of a certain wave phase. This script was written by Sebastian Rost.

combined_results_map.py plots the pierce point locations at the CMB.

sub_array_map.py created the map showing the centre points of the sub-arrays

pierce_point_map.py plots a map of pierce points at the CMB using just the station and event locations. These points are hence
imaged locations based on the PKP raypaths predicted by PREM
