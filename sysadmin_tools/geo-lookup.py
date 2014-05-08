# geo-lookup.py by iamrayw
# process csv by geo location
#
#   1. Save your IP addresses in a .csv file
#        -  name csv file "batch.csv"
#   2. Go to http://www.ipinfodb.com/ip_location_api.php and receieve your own API key
#   3. Update the config with your API key
#   4. Run the script
#   $ python geo-lookup.py
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
    return [ip_addr for ip_addr in batch]


def batch_process(batch):
    "Runs csv file through the IPInfoDB API"
    try:
        i = 0
        with open('output.csv', 'a') as f:
            output = csv.writer(f)
            for ipList in batch:
                for ip_addr in ipList:
                    print str(ip_addr)
                    response = urllib.urlopen(url + "&ip=" + str(ip_addr)).read()
                    tree = ET.fromstring(response)

                    outputToFile = []
                    for child in tree:
                        if child.tag == 'ipAddress':
                            outputToFile.append(str(child.text))
                        if child.tag == 'countryCode':
                            outputToFile.append(str(child.text))
                        if child.tag == 'timeZone':
                            outputToFile.append(str(child.text))
                    output.writerow(outputToFile)
                    i += 1
                    print "\t" + str(i) + " of " + str(len(batch)) + ":\t"

#        os.rename('output.txt', 'output.csv')
        print "Complete."
    except KeyboardInterrupt:
        print "\nExiting..."
        exit()


if __name__ == "__main__":
    base_url = "http://api.ipinfodb.com/v3/ip-city/?format=xml&key="
    url = base_url + key
    current_batch = get_batch(batch_filename)
    print "Added " + str(len(current_batch)) + " entries from " + str(batch_filename) + "\n"
    print "Working... This may take a while, please be patient.\n"
    batch_process(current_batch)
