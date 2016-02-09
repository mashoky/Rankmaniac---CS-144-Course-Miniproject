#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    #end = line.split(":")
    #vals = end[1].rstrip("\n").split( )
    #new_rank = float(vals[0]) * -1
    #sys.stdout.write("FinalRank:%f %d\n" % (new_rank, int(vals[1])))
    sys.stdout.write(line)

