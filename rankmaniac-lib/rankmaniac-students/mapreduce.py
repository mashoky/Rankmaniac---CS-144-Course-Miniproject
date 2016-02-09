#!/usr/bin/env python
from os import system

input_file = 'input.txt'
output_file = 'output.txt'
extra_file = 'input2.txt'
for num_iter in range(50):
    system('python data\pagerank_map.py < data\%s | sort | \
    python data\pagerank_reduce.py > data\%s' %(input_file,output_file))
    
    input_file = output_file
    temp = output_file
    output_file = extra_file
    extra_file = temp
system('python data\process_map.py < data\%s | sort | python data\process_reduce.py > data\%s' %('input2.txt', 'FinalOutput.txt'))
