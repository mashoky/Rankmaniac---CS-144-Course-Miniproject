#!/usr/bin/env python

import sys

large_num = 99999
#
# This program simply represents the identity function.
#
for line in sys.stdin:
    values = line.split("\t")
    iter = int(values[0].split( )[1])
    node_id = int(values[1])
    node_info = values[2].rstrip("\n").split( )
    if len(node_info) < 3:
        neighbors = ''
    else:
        neighbors = node_info[2]
    curr_rank = float(node_info[0])
    prev_rank = float(node_info[1])
    new_rank = large_num - curr_rank
    
    sys.stdout.write("LATER_ITER %f\t%d\t%d %f %s\n" % (new_rank, iter + 1, node_id,\
            large_num - prev_rank, neighbors))
    #end = line.split(":")
    #vals = end[1].rstrip("\n").split( )
    #new_rank = float(vals[0]) * -1
    #sys.stdout.write("FinalRank:%f %d\n" % (new_rank, int(vals[1])))
    #sys.stdout.write(line)

