#!/usr/bin/env bash
"""
Takes map_pierce_general.txt, runs it through TauP to produce cmb_lat and cmb_lon pierce points at the core-mantle boundary.
Script provided by Sebastian Rost & Jamie Ward
"""
#read in data to the terminal

input="map_pierce_general_2013_2014.csv"


#reads in data from the file loaded above as input

while read line

do

 evla=$(echo $line | awk '{print $3}')

 evlo=$(echo $line | awk '{print $4}')

 stla=$(echo $line | awk '{print $1}')

 stlo=$(echo $line | awk '{print $2}')

 evdp=$(echo $line | awk '{print $5}')

 

 #calculate the pierce points lon and lat using PKIKP data and the prem model

 cmb_lat=$(taup_pierce -mod prem -evt $evla $evlo -sta $stla $stlo -h $evdp -ph PKIKP -nodiscon -pierce 2891 | awk 'NR==2 {print $4}')

 cmb_lon=$(taup_pierce -mod prem -evt $evla $evlo -sta $stla $stlo -h $evdp  -ph PKIKP -nodiscon -pierce 2891 | awk 'NR==2 {print $5}')


 #print data to cmb_bouncepoints.txt

 echo $evla $evlo $stla $stlo $evdp $cmb_lat $cmb_lon


#close loop

done<$input >cmb_bouncepoint_to_plot_2013_2014_source_side.txt
