#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

In a python list how to use the double colon [::]?

En una lista python ¿como se usa el doble dos puntos [::]?
'''

#create a list
lista = [1, 4, 7, 3, 9, 10, 6, 5, 2, 8, 11]
print (lista)

#list[start:stop:step]
#step specify an increment between the elements to cut of the list.
sublist = lista[2:9:2]
print(sublist)

#returns a list with a jump every 3 items.
sublist = lista[::4]
print(sublist)

#when step is negative the jump is made back
sublist = lista[10:2:-3]
print(sublist)
