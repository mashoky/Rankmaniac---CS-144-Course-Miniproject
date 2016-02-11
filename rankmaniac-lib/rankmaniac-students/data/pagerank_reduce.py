#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
final = []
sum = 0
prev_idx = -1
changed = False
print_buffer = []
for line in sys.stdin:
    #sys.stdout.write('Line:%s' %line)
    values = line.split("\t")
    iter = int(values[0].split( )[1])
    node_idx = int(values[0].split( )[0])
    node_info = values[1].rstrip("\n").split( )
    if node_idx == prev_idx or prev_idx == -1:
        sum += float(node_info[0])
        prev_rank = float(node_info[1])
        if(len(node_info) < 3):
            prev_info = ''
        else:
            prev_info = node_info[2]

    else:      
        new_rank = (0.85 * sum) + 0.15
        #print 'Change' + str(changed)
        #print prev_info
        if iter < 50:    
            sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (iter + 1, prev_idx,\
            new_rank, prev_rank, prev_info))
        else:
            final.append("FinalRank:%f\t%d\n" % (new_rank, prev_idx))
        #else:
        #    print_buffer.append("%d\t%f %f %s" % (prev_idx, new_rank, prev_rank, prev_info))
        #sys.stdout.write("FinalRank:%f\t%s" % (float(new_rank), str(prev_idx)))
        #sys.stdout.write("%d\t%f %f %s" % (prev_idx, new_rank, prev_rank, prev_info))
        
        sum = 0
        sum += float(node_info[0])
        prev_rank = float(node_info[1])
        if(len(node_info) < 3):
            prev_info = ''
        else:
            prev_info = node_info[2]
    prev_idx = node_idx
new_rank = (0.85 * sum) + 0.15
if iter < 50:    
    sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (iter + 1, prev_idx, new_rank,\
    prev_rank, prev_info))
else:
    final.append("FinalRank:%f\t%d\n" % (new_rank, prev_idx))
if len(final) >= 20:
    for i in range(20):
        sys.stdout.write(max(final))
        final.remove(max(final))
        #sys.stdout.write(i)

