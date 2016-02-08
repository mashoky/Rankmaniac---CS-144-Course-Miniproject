#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
sum = 0
prev_idx = -1
changed = False
print_buffer = []
for line in sys.stdin:
    sys.stdout.write(line)
    values = line.split("\t")
    node_idx = int(values[0])
    node_info = values[1].split( )
    #print len(node_info)
    if node_idx == prev_idx or prev_idx == -1:
        #print values[1]
        sum += float(node_info[0])
        prev_rank = float(node_info[1])
        prev_info = node_info[2]
    else:      
        new_rank = (0.85 * sum) + 0.15
        if new_rank != prev_rank:
            changed = True
        if changed:
            #sys.stdout.write("%d\t%f %f %s" % (prev_idx, new_rank, prev_rank, prev_info))
            pass
        else:
            print_buffer.append("%d\t%f %f %s" % (prev_idx, new_rank, prev_rank, prev_info))
        #sys.stdout.write("FinalRank:%f\t%s" % (float(new_rank), str(prev_idx)))
        #sys.stdout.write("%d\t%f %f %s" % (prev_idx, new_rank, prev_rank, prev_info))
        
        sum = 0
        sum += float(values[1])
    prev_idx = node_idx

