#!/usr/bin/env python

import sys
import Queue

#
# This program simply represents the identity function.
#

rank_count = 0
lines = []
for line in sys.stdin:
    sys.stdout.write(line)
    if line.startswith("F"):
        sys.stdout.write('here')        
        if rank_count < 20:
            end = line.split(":")
            vals = end[1].rstrip("\n").split( )
            new_rank = float(vals[0]) * -1
            sys.stdout.write("FinalRank:%f %d\n" % (new_rank, int(vals[1])))
        rank_count += 1
    else:
        sys.stdout.write(line)
#    lines.append(line)
#for i in range(20):
    #sys.stdout.write(lines.pop())
    
    #if (line.startswith("FinalRank")):
    #    line = line.split(":")
    #    rank = line[1].split("\t")
    #    #print line[1]
    #    sys.stdout.write("FinalRank:%f\t%s\n" % (abs(float(rank[0])), rank[1]))
    #else:
    #    sys.stdout.write(line)

    

