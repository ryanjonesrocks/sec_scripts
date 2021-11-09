#!/bin/bash

# Add subnets here
declare -a varname
subnet_array=( 
# 0.0.0.0/0
)

for val in ${subnet_array[@]}; do
   masscan $val -p80,443,8080,8443,81, 4444, 4443, 8888 >> massscan_open_ports
done
