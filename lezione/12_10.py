# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:21:59 2021

@author: danie
"""

import turtle


from random import random

def draw_tree(cursor, leng, level, is_color = False):
    if is_color:
        r, g, b = random(), random(), random()
        cursor.pencolor(r, g, b)
    cursor.pendown()
    cursor.fd(leng)
    if level >1:
        draw_tree(cursor, leng*0.8, level - 1, is_color = is_color)
        cursor.right(30+30)
        draw_tree(cursor, leng*0.8, level - 1, is_color = is_color)
        cursor.lt(30)
    else:
        cursor.stamp()
    cursor.penup()
    cursor.backward(leng)
    
    
    
    
    