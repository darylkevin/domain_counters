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
            # Slice domain names to obtain subdomains
            for i in range(len(full_domain)):
                if full_domain[i] == '.':
                    sub_domain = full_domain[i+1:]
                    if sub_domain not in domains:
                        domains[sub_domain] = int(count)
                    elif sub_domain in domains:
                        domains[full_domain[i+1:]] += int(count)
        # Sorts our output based from highest clicks to lowest
        # Defines our key for sorting which is the clicks count
        for k,v in sorted(domains.items(), key=by_value, reverse=True):
            print(f'{v}\t{k}')


if __name__ == '__main__':
    domain_counter('input.csv')
