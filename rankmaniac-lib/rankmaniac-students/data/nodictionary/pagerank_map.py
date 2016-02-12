#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

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
            neighbors = map(int,node_info[2].split(","))
        curr_rank = float(node_info[0])

        num_neighbors = len(neighbors)
        for n in neighbors:
            sys.stdout.write("%d %d %d\t%f %f\n" % (n, node_id, iter, curr_rank / num_neighbors, \
            curr_rank))   
            
    else:
        
        values = line.split("\t")
        beginning = values[0].split(":")
        node_id = int(beginning[1])
        node_info = values[1].rstrip("\n").split(",")
        if len(node_info) < 3:
            neighbors = []
        else:
            neighbors = map(int,node_info[2].split(","))
        curr_rank = float(node_info[0])

        num_neighbors = len(neighbors)
        if num_neighbors == 0:
            sys.stdout.write("%d %d %d\t%f %f\n" %(node_id, node_id, iter, curr_rank, curr_rank))
        for n in neighbors:
            sys.stdout.write("%d %d %d\t%f %f\n" % (n, node_id, iter, curr_rank / num_neighbors, \
            curr_rank))     

