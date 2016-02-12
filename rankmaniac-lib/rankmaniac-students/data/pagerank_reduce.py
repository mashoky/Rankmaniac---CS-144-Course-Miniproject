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

prev_info = ''
curr_info = ''
itern = -1
prev_rank = -1
prev_empty = False
for line in sys.stdin:
    if line.endswith('Node_info\n'):
        values = line.split("\t")
        ending = values[1].split( )
        #if prev_info != '' and len(ending) > 1:
        #    curr_info = ending[0]
        #if len(ending) > 1:    
        #    prev_info = ending[0]
        #else:
        #    prev_info = ''
        if prev_info != '' or (prev_info == '' and prev_empty):
            new_rank = (0.85 * sum) + 0.15
            sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern + 1, prev_idx,\
                new_rank, prev_rank, prev_info))     
            sum = 0
            prev_idx = int(values[0])
            prev_empty = False
        if len(ending) > 1:    
            prev_info = ending[0]
        else:
            prev_info = ''  
            prev_empty = True      
    else:
        values = line.split("\t")
        node_idx = int(values[0])
        node_info = values[1].rstrip("\n").split( )
        itern = int(node_info[0])
        if node_idx == prev_idx or prev_idx == -1:
            sum += float(node_info[1])
            prev_rank = float(node_info[2])
    
        else:     
            new_rank = (0.85 * sum) + 0.15
            sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern + 1, prev_idx,\
                new_rank, prev_rank, prev_info))
            
            sum = 0
            sum += float(node_info[0])
            prev_rank = float(node_info[1])
            #if curr_info != '':
            #    prev_info = curr_info
            #    curr_info = ''
            #else:
            #    prev_info = ''
            prev_info = ''
            prev_empty = False
        prev_idx = node_idx
new_rank = (0.85 * sum) + 0.15
   
sys.stdout.write("LATER_ITER %d\t%d\t%f %f %s\n" % (itern + 1, prev_idx, new_rank, prev_rank, prev_info))
