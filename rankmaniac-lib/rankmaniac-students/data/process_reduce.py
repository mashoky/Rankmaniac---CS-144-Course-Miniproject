#!/usr/bin/env python

import sys
import Queue

#
# This program simply represents the identity function.
#

rank_count = 0
lines = []
for line in sys.stdin:
    #if rank_count < 20:
    #    end = line.split(":")
    #    vals = end[1].rstrip("\n").split( )
    #    new_rank = float(vals[0]) * -1
    #    sys.stdout.write("FinalRank:%f %d\n" % (new_rank, int(vals[1])))
    #rank_count += 1
#    lines.append(line)
#for i in range(20):
    #sys.stdout.write(lines.pop())
    sys.stdout.write(line)
    

