#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

data = {}
for line in sys.stdin:
    #sys.stdout.write(line)
    if line.startswith('LATER_ITER'):
        pass 
            
    else:
        values = line.split("\t")
        beginning = values[0].split(":")
        node_id = int(beginning[1])
        node_info = map(float, values[1].rstrip("\n").split(","))
        neighbors = node_info[2:-1]
        curr_rank = node_info[0]
        prev_rank = node_info[1]
        num_neighbors = len(neighbors)
        data[node_id] = (curr_rank,prev_rank, neighbors)
for node in data.itervalues():
    for n in node[2]:
        p_rank = data[n][1]
        n_neighbors = data[n][2]
        sys.stdout.write("%d\t%f%f%s\n" % (n, curr_rank / num_neighbors, \
        p_rank, ''.join(str(id) for id in n_neighbors) ))        
        
