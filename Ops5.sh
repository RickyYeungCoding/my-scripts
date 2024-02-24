#!/bin/bash

# Script Name:                  Ops challenge 05
# Author:                       Ricky Yeung
# Date of latest revision:      2/23/24
# Purpose:                      Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.


# Main
while true; do
# Display running processes
echo "Running Processes:"
ps aux

# Ask the user for a PID
read -p "Enter PID to kill (Ctrl + C to exit): " pid_to_kill
# Check if the input is a valid integer
if [[ $pid_to_kill =~ ^[0-9]+$ ]]; then
# Check if the process is not essential for OS functionality
if [ $pid_to_kill -ne $$ ]; then
# Kill the process
kill -15 $pid_to_kill
echo "Process with PID $pid_to_kill terminated."
else
echo "Cannot terminate essential processes."
fi
else
echo "Invalid input. Please enter a valid PID."
fi
done