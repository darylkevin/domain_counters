import csv

# Dictionary to be used for storing domain names and value pairs 
# (number of hits)
domains = {}

# Defines criteria for sorting out dictionary items from highest to lowest
def by_value(item):
    return item[1]

# Main function for sorting out domain hits
