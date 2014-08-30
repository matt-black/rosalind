# -*- coding: utf-8 -*-
"""
Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
"""

from __future__ import print_function
from re import findall

def file_read(f):
    """Read in file"""
    set_list = []
    for i, line in enumerate(f):
        if i == 0:
            n = int(line.rstrip())
        else:
            set_list.append(findall('\d+', line))
            set_list[i-1] = map(int,set_list[i-1])
    return n, set_list

f = open('rosalind_seto.txt','r')
n, sets = file_read(f)
f.close()
sets = map(set,sets)  #convert to sets

#calculate attributes of sets
union = sets[0].union(sets[1])
intersection = sets[0].intersection(sets[1])
a_min_b = sets[0].difference(sets[1])
b_min_a = sets[1].difference(sets[0])

#calculate complements
comp_set = {i for i in range(1,n+1)}
a_comp = comp_set.difference(sets[0])
b_comp = comp_set.difference(sets[1])

def set_printer(set_in,f):
    nums = tuple(set_in)
    print('{', nums[0], sep='', end=', ', file=f)
    for num in nums[1:-1]:
        print(num, end=', ', file=f)
    print(nums[-1],end='}\n', file=f)

f_out = open('seto_answer.txt','w')
set_printer(union,f_out)
set_printer(intersection,f_out)
set_printer(a_min_b,f_out)
set_printer(b_min_a,f_out)
set_printer(a_comp,f_out)
set_printer(b_comp,f_out)
f_out.close()