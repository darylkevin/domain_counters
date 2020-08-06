import csv

# Dictionary to be used for storing domain names and value pairs 
# (number of hits)
domains = {}

# Defines criteria for sorting out dictionary items from highest to lowest
def by_value(item):
    return item[1]

# Main function for sorting out domain hits
def domain_counter(file):
    with open(file) as csvfile:
        domain_file = csv.reader(csvfile, delimiter=',')
        # Defines domain names and click count from csv
        for row in domain_file:
            full_domain = row[1]
            count = row[0]
            # Adds keys to our domains dictionary
            if full_domain not in domains:
                domains[full_domain] = int(count)
            elif full_domain in domains:
                domains[full_domain] += int(count)
