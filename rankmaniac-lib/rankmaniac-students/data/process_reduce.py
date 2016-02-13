#!/usr/bin/env python

import sys
import Queue

#
# This program simply represents the identity function.
#

rank_count = 0
lines = []
final = []
    

large_num = 99999
num_printed = 0

end = True
for line in sys.stdin:
    if line.endswith('Node_info\n'):
        lines.append(line)
    else:
        values = line.split("\t")
        curr = float(values[0].split( )[1])
        itern = int(values[1])
        node_info = values[2].rstrip("\n").split( )
        if len(node_info) < 3:
            neighbors = ''
        else:
            neighbors = node_info[2]
        node_id = int(node_info[0])
        prev = float(node_info[1])
        diff = abs(curr - prev)
        
        if itern >= 50 :
            sys.stdout.write("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
            num_printed += 1
        
        elif rank_count < 30:
            if diff > 0.01:
                sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern,node_id, large_num - curr, large_num - prev, neighbors))
                end = False
                rank_count = 30
            else:
                lines.append("LATER_ITER %d\t%d\t%f %f %s\n" % (itern, node_id, large_num - curr, large_num - prev, neighbors))
                final.append("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
        else:
            if end:
                #sys.stdout.write("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
                break
            else:
                sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern,node_id, large_num - curr, large_num - prev, neighbors))
        if num_printed >= 20:
            break
        rank_count += 1
if end == True and itern < 50:
    for i in range(20):
        sys.stdout.write(final[i])    
else:  
    for line in lines:
        sys.stdout.write(line)

