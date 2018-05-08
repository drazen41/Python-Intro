# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here
infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename,'w')

for line in infile:
    striped = line.strip("\n")
    outfile.write(str(len(striped)) + "\n")
    
    
infile.close()
outfile.close()