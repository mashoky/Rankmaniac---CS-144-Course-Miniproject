#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

data = {}
itern = 1

for line in sys.stdin:
    #sys.stdout.write(line)
    if line.startswith('LATER_ITER'):
        values = line.split("\t")
        itern = int(values[0].split( )[1])
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
        if len(node_info) < 3:
            neighbors = []
        data[node_id] = (curr_rank,prev_rank, neighbors)

for key, node in data.iteritems():
    if len(node[2]) == 0:
        sys.stdout.write("%d %d\t%f %f %s\n" %(key, itern, node[0], node[0],""))
    for n in node[2]:
        n_neighbors = data[n][2]
        curr_rank = node[0]
        num_neighbors = len(node[2])
        sys.stdout.write("%d %d\t%f %f %s\n" % (n, itern, curr_rank / num_neighbors, \
        curr_rank, ','.join(str(id) for id in n_neighbors)))     

