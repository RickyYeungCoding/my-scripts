#!/bin/bash

# Script Name:                  Ops challenge 03
# Author:                       Ricky Yeung
# Date of latest revision:      2/21/24
# Purpose:                      Call function 3 times

# Declaration of variables
greeting="helloworld from Ricky"
# Declaration of functions

# Define Variables

# Declare Functions
print_login_history() {
    last | head -n 3
}
# Main
print_login_history
print_login_history
print_login_history

echo "This is the login history"
# End