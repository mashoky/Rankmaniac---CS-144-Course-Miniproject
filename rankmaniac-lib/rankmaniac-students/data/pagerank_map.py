#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

data = {}
iter = 1
for line in sys.stdin:
    #sys.stdout.write(line)
    if line.startswith('LATER_ITER'):
        values = line.split("\t")
        iter = int(values[0].split( )[1])
        node_id = int(values[1])
        node_info = values[2].rstrip("\n").split( )
        if len(node_info) < 3:
            neighbors = []
        else:
            neighbors = map(int, node_info[2].split(","))
        curr_rank = float(node_info[0])
        prev_rank = float(node_info[1])
        num_neighbors = len(neighbors)
        data[node_id] = (curr_rank,prev_rank, neighbors)
            
    else:
        
        values = line.split("\t")
        beginning = values[0].split(":")
        node_id = int(beginning[1])
        node_info = values[1].rstrip("\n").split(",")
        neighbors = map(int, node_info[2:])
        curr_rank = float(node_info[0])
        prev_rank = float(node_info[1])
        num_neighbors = len(neighbors)
        data[node_id] = (curr_rank,prev_rank, neighbors)

for node in data.itervalues():
    for n in node[2]:
        p_rank = data[n][1]
        n_neighbors = data[n][2]
        curr_rank = node[0]
        num_neighbors = len(node[2])
        sys.stdout.write("%d %d\t%f %f %s\n" % (n, iter, curr_rank / num_neighbors, \
        curr_rank, ','.join(str(id) for id in n_neighbors)))     

