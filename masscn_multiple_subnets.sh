#!/bin/bash

# Add subnets here
declare -a varname
subnet_array=( 
# 0.0.0.0/0
)

for val in ${subnet_array[@]}; do
   massscan $val -p 80,443, 8080, 8443, 81 >> massscan_open_ports
done
