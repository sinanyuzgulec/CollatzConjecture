#!/usr/bin/env python
# -*- coding: utf-8 -*- 
num = int(input("sayı girin: "))
def collatz(num):
    num_seq = [num]
    if num < 1:
       return []
    while num > 1:
       if num % 2 == 0:
         num = num / 2
       else:
         num = 3 * num + 1
       num_seq.append(num)    
    return num_seq

print(collatz(num))
