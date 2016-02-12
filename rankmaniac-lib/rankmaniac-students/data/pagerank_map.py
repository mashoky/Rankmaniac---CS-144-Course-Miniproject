#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

data = {}
itern = 1


for line in sys.stdin:
    #sys.stdout.write(line)
    #if line.endswith("Node_info\n"):
    #    sys.stdout.write(line)
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
        if num_neighbors == 0:
            sys.stdout.write("%d\t%d %f %f\n" %(node_id, itern, curr_rank, curr_rank))
            sys.stdout.write('%d\tNode_info\n' % (node_id))
        else:
            sys.stdout.write('%d\t%s Node_info\n' % (node_id, ','.join(str(i) for i in neighbors)))
        for n in neighbors:
            sys.stdout.write("%d\t%d %f %f\n" % (n, itern, curr_rank / num_neighbors, \
            curr_rank))  


            
    else:        
        values = line.split("\t")
        beginning = values[0].split(":")
        node_id = int(beginning[1])
        node_info = values[1].rstrip("\n").split(",")
        if len(node_info) < 3:
            neighbors = []
        else:
            neighbors = map(int, node_info[2:])
        curr_rank = float(node_info[0])
        prev_rank = float(node_info[1])
        num_neighbors = len(neighbors)
        if num_neighbors == 0:
            sys.stdout.write("%d\t%d %f %f\n" %(node_id, itern, curr_rank, curr_rank))
            sys.stdout.write('%d\tNode_info\n' % (node_id))
        else:
            sys.stdout.write('%d\t%s Node_info\n' % (node_id, ','.join(str(i) for i in neighbors)))
        for n in neighbors:
            sys.stdout.write("%d\t%d %f %f\n" % (n, itern, curr_rank / num_neighbors, \
            curr_rank))    
        