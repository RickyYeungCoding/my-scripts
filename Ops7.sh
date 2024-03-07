#!/bin/bash
# Script Name:                  Ops challenge 07
# Author:                       Ricky Yeung
# Date of latest revision:      2/27/24
# Purpose:                      Display System Information
#Execution:                     bash ./Ops7.sh
# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this script as root using sudo."
  exit 1
fi

# Function to display information for a specific component
display_component_info() {
  echo "------------------------"
  echo " $1 Information"
  echo "------------------------"
  lshw -class $2 | grep -E "description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources" | sed 's/^[ \t]*//'
  echo
}

# Display system information for each component
for component in "computer" "processor" "memory" "display" "network"; do
  display_component_info "$component" "$component"
done