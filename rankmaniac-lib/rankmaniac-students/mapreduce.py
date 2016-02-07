#!/usr/bin/env python
from os import system

for iter_num in range(50):
    system('python data\pagerank_map.py < data\input.txt | sort | \
    python data\pagerank_reduce.py | python data\process_map.py | sort | \
    python data\process_reduce.py > data\output.txt')
