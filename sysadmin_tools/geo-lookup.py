# geo-lookup.py by iamrayw
# process csv by geo location
#
#   1. Save your user email and IP addresses in a .csv file
#        -  Each email and IP should be in its own column in Excel (or separated by commas)
#        -  Enter the name of your .csv file:
#   2. Go to http://www.ipinfodb.com/ip_location_api.php and get your own API key
#   3. Update the config with your API key:
#   4. Run the script:
#   $ python ip_lookup.py
batch_filename = "batch.csv"
key = "9180559212c309581050c846fe426c41e48cfd67c4fb8fd3f00a79b37cf6b524"

import xml.etree.ElementTree as ET
import urllib
import csv
import os


# Process csv into list batch
def get_batch(batch_filename):
    "Creates list containing all the IP addresses from your batch file"
    batch = csv.reader(open(batch_filename))#, delimiter=',')
    return [[ip_addr] for ip_addr in batch]


def batch_process(batch):
    "Runs csv file through the IPInfoDB API"
    try:
        i = 0
        output = open('output.txt', 'a')
        for ip_addr in batch:
            response = urllib.urlopen(url + "&ip=" + str(ip_addr)).read()
            tree = ET.fromstring(response)

            output.write(",")
            for child in tree:
                if child.tag == 'ipAddress':
                    output.write(str(child.text) + ",")
                if child.tag == 'countryCode':
                    output.write(str(child.text) + ",")
                if child.tag == 'timeZone':
                    output.write(str(child.text) + "\n")
            i += 1
            print "\t" + str(i) + " of " + str(len(batch)) + ":\t"
        output.close()
        os.rename('output.txt', 'output.csv')
        print "Complete."
    except KeyboardInterrupt:
        output.close()
        print "\nExiting..."

base_url = "http://api.ipinfodb.com/v3/ip-city/?format=xml&key="
url = base_url + key
current_batch = get_batch(batch_filename)

print "Added " + str(len(current_batch)) + " entries from " + str(batch_filename) + "\n"
print "Working... This may take a while, please be patient.\n"

batch_process(current_batch)