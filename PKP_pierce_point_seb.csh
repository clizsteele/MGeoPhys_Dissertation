#!/bin/csh
# needs taup toolkit 2.6.1
# Sebastian Rost (Leeds) - 14.03.2023
# Usage PKP_pierce_point.csh slowness backazimuth sourcelat sourcelon


set taup_261_path = "/nfs/a301/ee19ces/diss/codes/TauP-2.6.1-SNAPSHOT/bin"

set slown = $1
set baz = $2
set slat = $3
set slon = $4

# first call to get distance from slowness (but does not give location)

${taup_261_path}/taup_pierce -mod prem -h 10  -sta $slat $slon -baz $baz --shootray $slown -ph PKP >! dummy

set max = ` wc -l dummy | awk '{print $1}' `
set dist = ` awk 'NR=='$max' {print $1}' dummy `

# second call for location
${taup_261_path}/taup_pierce -mod prem -h 0 -sta $slat $slon -baz $baz -deg $dist -ph PKP -pierce 2889 -nodiscon >! dummy

set ab_lat_1 = ` awk 'NR==2 {print $4}' dummy `
set ab_lon_1 = ` awk 'NR==2 {print $5}' dummy `
set ab_lat_2 = ` awk 'NR==3 {print $4}' dummy `
set ab_lon_2 = ` awk 'NR==3 {print $5}' dummy `
set bc_lat_1 = ` awk 'NR==5 {print $4}' dummy `
set bc_lon_1 = ` awk 'NR==5 {print $5}' dummy `
set bc_lat_2 = ` awk 'NR==6 {print $4}' dummy `
set bc_lon_2 = ` awk 'NR==6 {print $5}' dummy `

\rm dummy
echo BC Lat/Lon Receiver Side: $bc_lat_1, $bc_lon_1
echo BC Lat/Lon Source Side: $bc_lat_2, $bc_lon_2
echo AB Lat/Lon Receiver Side: $ab_lat_1, $ab_lon_1
echo AB Lat/Lon Source Side: $ab_lat_2, $ab_lon_2
