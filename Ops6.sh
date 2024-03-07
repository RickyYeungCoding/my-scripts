#!/bin/bash

# Script Name:                  Ops challenge 006
# Author:                       Ricky Yeung
# Date of latest revision:      2/26/24
# Purpose:                      Write a script that detects if a file or directory exists and creates it if it does not exist


# Example array of file or directory paths
paths_to_create=("example_directory1" "example_directory2" "example_file.txt")

# Loop through the array and create each file or directory
for path in "${paths_to_create[@]}"; do
if [ ! -e "$path" ]; then
mkdir -p "$path"
echo "$path created successfully."
else
echo "$path already exists."
fi
done

#Notes
This line starts a for loop, iterating through each element in the array paths_to_create. The current element is stored in the variable path.
This line checks if the file or directory specified by the current path does not exist 
If the condition in the previous line is true (i.e., the file or directory does not exist), these lines create the file or directory using mkdir -p "$path" and print a success message.
If the condition in the if statement is false (i.e., the file or directory exists), this line prints a message indicating that the path already exists.
This line marks the end of the if-else block and the end of the for loop. 