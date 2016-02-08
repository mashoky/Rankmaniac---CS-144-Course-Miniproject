#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
sum = 0
node_idx = 0
for line in sys.stdin:
    sys.stdout.write(line)
    values = line.split("\t")
    node_idx = int(values[0])
    
    sum += float(values[1])
new_rank = (0.85 * sum) + 0.15
sys.stdout.write("FinalRank:%f\t%s" % (float(node_idx), str(new_rank)))
#    

