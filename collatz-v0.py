#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Collatz sanısı v 0
sayi = int(input("sayı girin: "))
def collatz(sayi):
    sayi_listesi = [sayi]
    if sayi < 1:
       return []
    while sayi > 1:
       if sayi % 2 == 0:
         sayi = sayi / 2
       else:
         sayi = 3 * sayi + 1
       sayi_listesi.append(sayi)    
    return sayi_listesi

print(collatz(sayi))
