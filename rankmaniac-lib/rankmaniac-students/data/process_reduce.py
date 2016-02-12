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

end = True
for line in sys.stdin:
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
    
    if itern > 50:
       sys.stdout.write("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
    
    elif rank_count < 30:
        if diff > 0.01:
            end = False
        else:
            lines.append("LATER_ITER %d\t%d\t%f %f %s\n" % (itern, node_id, large_num - curr, large_num - prev, neighbors))
            final.append("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
    else:
        if end:
            sys.stdout.write("FinalRank:%f\t%s\n" % (large_num - curr, str(node_id)))
        else:
            sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern,node_id, large_num - curr, large_num - prev, neighbors))
    rank_count += 1
    #if rank_count < 20:
    #    end = line.split(":")
    #    vals = end[1].rstrip("\n").split( )
    #    new_rank = float(vals[0]) * -1
    #    sys.stdout.write("FinalRank:%f %d\n" % (new_rank, int(vals[1])))
    #rank_count += 1
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
    #sys.stdout.write(line)
if end:
    for line in lines:
        sys.stdout.write(line)
else:
    for line in final:
        sys.stdout.write(line)

