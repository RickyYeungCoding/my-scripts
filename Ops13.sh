#!/bin/bash
# Script Name:                  Ops challenge 13
# Author:                       Ricky Yeung
# Date of latest revision:      3/6/24
# Purpose:                      Domain Analyzer

get_domain_info() {
    read -p "Enter a domain: " domain

    if [[ $domain != "" ]]; then
        # Run whois
        echo "Fetching whois information for $domain..."
        whois $domain 

        # Run dig
        echo "Fetching dig information for $domain..."
        dig $domain 

        # Run host
        echo "Fetching host information for $domain..."
        host $domain 

        # Run nslookup
        echo "Fetching nslookup information for $domain..."
        nslookup $domain 
    fi
}
get_domain_info