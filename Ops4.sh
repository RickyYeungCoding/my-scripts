#!/bin/bash

# Script Name:                  Ops challenge 04
# Author:                       Ricky Yeung
# Date of latest revision:      2/22/24
# Purpose:                      Array Challenge
#Execution:                     bash ./Ops4.sh
# Declaration of variables
directories=("dir1" "dir2" "dir3" "dir4")
# Index         0      1     2      3
# Length = 4
# Index  = 0-3

# Display the INdex of the Directories Array
echo "the first directory in the directories array is: ${directories[0]}" # -> dir1
echo "the first directory in the directories array is: ${directories[1]}"
echo "the first directory in the directories array is: ${directories[2]}"
echo "the first directory in the directories array is: ${directories[3]}"

# Create directories
for dir in "${directories[@]}"; do
    mkdir "$dir"
done

# Create .txt file in each directory using array indices
for ((i=0; i<${#directories[@]}; i++)); do
    touch "${directories[i]}/file.txt"
done

# Display a message for validation
echo "Script executed successfully. Directories and files created:"
ls -R
