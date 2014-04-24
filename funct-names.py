#!/usr/bin/env python
__author__ = 'jmmnn'
# this script filters first names from the social security admin source: http://www.ssa.gov/oact/babynames/limits.html

import sys
import csv
import os
import glob

filteredNames = []
def concatFiles():
    for filename in glob.glob(os.path.join('names/', '*.txt')):
        # do your stuff
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            #keep only 4 letter names, not ending with "i" or "y"
            for row in reader:
                if row[1] == 'F' and 3 < len(row[0]) < 5 and not(row[0].endswith('i')) and not(row[0].endswith('y')):
                    filteredNames.append(row[0])
    return filteredNames

#execute concatenation
concatFiles()

#verify 1st filtering
#print filteredNames

#sorting, this works but is not being used
#sortedNames = sorted(filteredNames, key=lambda item: item[0])

#verify sorting
#print sortedNames

#removing duplicates and sort
uniqueNames = sorted(set(filteredNames))

#remove [ and , and print a human readable list
for name in uniqueNames:
    print '\t' , name

# count them
print '\n' , "total # of names : " , len(uniqueNames)
