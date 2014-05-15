#cc_scrub v2.4
# cc_scrubV2.4.py by iamrayw
#runs aginst directory for 1foonumber hashes out lines 15-23 & 27-30 / afoonumber12 hashes out lines 17-25 & 29-32
#to use replace 1foonumber & afoonumber12 with variables you want to hash and adjusted line variable #

import os
import re
#import tarfile


def replaceCC(logFile):

    with open(logFile) as f:
        fixedLog = ""
        for line in f:
            fixedLog += re.sub(r'(\d{5})\d{8}(\d{3})', r'\1########\2', line)

    with open(logFile, "w") as f:
        f.write(fixedLog)


def replaceCVV(logFile):

    with open(logFile) as f:
        fixedLog = ""
        for line in f:
            index = line.rfind("1foonumber=")
            if index > 1:
                fixedLog += line[:index+27] + "###" + line[index+30:]
            else:
                fixedLog += line
 
    with open(logFile, "w") as f:
        f.write(fixedLog)


def replaceCC2(logFile):

    with open(logFile) as f:
        fixedLog = ""
        for line in f:
            index = line.rfind("afoonumber12=")
            if index > 1:
                fixedLog += line[:index+17] + "###" + line[index+25:]
            else:
                fixedLog += line
 
    with open(logFile, "w") as f:
        f.write(fixedLog)


def replaceCVV2(logFile):

    with open(logFile) as f:
        fixedLog = ""
        for line in f:
            index = line.rfind("afoonumber12=")
            if index > 1:
                fixedLog += line[:index+29] + "###" + line[index+32:]
            else:
                fixedLog += line
 
    with open(logFile, "w") as f:
        f.write(fixedLog)


if __name__ == "__main__":
    for root, directory, files in os.walk("/var/log/syslog/mylogs/"):
        for eachFile in files:
            print "Processing file %s" % (os.path.join(root, eachFile))
            replaceCC(os.path.join(root, eachFile))
            replaceCVV(os.path.join(root, eachFile))
            replaceCC2(os.path.join(root, eachFile))
            replaceCVV2(os.path.join(root, eachFile))
        print "Done!"
