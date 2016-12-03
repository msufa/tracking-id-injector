#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print('usage: python {} input_filename output_filename'.format(sys.argv[0]))
    exit(1)

with open(sys.argv[1], 'r') as infile:
    with open(sys.argv[2], 'w') as outfile:
        outfile.write(infile.read())
