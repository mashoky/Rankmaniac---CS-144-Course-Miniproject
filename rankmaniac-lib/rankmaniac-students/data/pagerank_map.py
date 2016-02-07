#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    #sys.stdout.write(line)
    values = line.split("\t")
    beginning = values[0].split(":")
    node_id = int(beginning[1])
    node_info = map(float, values[1].rstrip("\n").split(","))
    neighbors = node_info[2:-1]
    curr_rank = node_info[0]
    num_neighbors = len(neighbors)
    for n in neighbors:
        sys.stdout.write("%d\t%f" % (n, curr_rank / num_neighbors))
