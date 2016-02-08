#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
sum = 0
prev_idx = -1
for line in sys.stdin:
    sys.stdout.write(line)
    values = line.split("\t")
    node_idx = int(values[0])
    if node_idx == prev_idx or prev_idx == -1:
        sum += float(values[1])
    else:      
        new_rank = (0.85 * sum) + 0.15
        sys.stdout.write("FinalRank:%f\t%s" % (float(new_rank), str(prev_idx)))
        sum = 0
        sum += float(values[1])
    prev_idx = node_idx

