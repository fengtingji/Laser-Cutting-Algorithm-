# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:07:45 2017

@author: Fengting Ji
"""

import numpy as np
#Independent input parameters
#Box dimension
length = 3.0
width = 3.5
height = 3.5
#Close or open box
Close = False
#Material thickness
thickness = 1.0 / 8
#Nut and screw dimensions
nutwidth = 1.0 / 4
nutheight = 3.0 / 32
screwlength = 1.0 / 2
screwdiameter = 0.008 + 0.112
#Laser kerf
kerf = 0.005
#Output location
loc = "C:/Users/Fengting Ji/Desktop/"
#Check input validity
if width * 2 > 11.5 or height + width > 11.5:
   print("Box dimensions too large.")
   exit()
if width < 3.0 or height < 3.0 or length < 3.0:
   print("Box dimensions too small.")
   exit()
if thickness >= nutwidth:
   print("Thickness should be smaller than nut width.")
   exit()
if screwlength <= nutwidth:
   print("Use longer screw.")
   exit()
#Dependent parameters
#Number of steps
n1 = (int(length) - 1) * 2 + 1
n2 = (int(width) - 1) * 2 + 1
n3 = (int(height) - 1) * 2 + 1
#Tap width
screwtab = 2.0 * nutwidth
tab1 = (length - 4 * screwtab) / (n1 - 4) * 90
tab2 = (width - 4 * screwtab) / (n2 - 4) * 90
tab3 = (height - 4 * screwtab - 2 * thickness) / (n3 - 4) * 90
tab2k = (width + 2 * kerf - 4 * screwtab) / (n2 - 4) * 90
tab3k = (height + 2 * kerf - 4 * screwtab - 2 * thickness) / (n3 - 4) * 90
#Multiply by 90 for larger numerical number and easier understanding
t = thickness * 90
a = screwtab * 90
b = (screwtab - screwdiameter) / 2 * 90
c = screwdiameter * 90
d = screwlength * 90
e = (d - t - nutheight * 90) / 2
f = (nutwidth - screwdiameter) / 2 * 90
g = nutheight * 90
#Trajectory of t slot towards left
def lslot(x, y):
    list_lslot = []
    x = x - t
    list_lslot.append((x, y))
    y = y + b
    list_lslot.append((x, y))
    x = x - e
    list_lslot.append((x, y))
    y = y - f
    list_lslot.append((x, y))
    x = x - g
    list_lslot.append((x, y))
    y = y + f
    list_lslot.append((x, y))
    x = x - e
    list_lslot.append((x, y))
    y = y + c
    list_lslot.append((x, y))
    x = x + e
    list_lslot.append((x, y))
    y = y + f
    list_lslot.append((x, y))
    x = x + g
    list_lslot.append((x, y))
    y = y - f
    list_lslot.append((x, y))
    x = x + e
    list_lslot.append((x, y))
    y = y + b
    list_lslot.append((x, y))
    x = x + t
    list_lslot.append((x, y))
    return list_lslot
#Trajectory of t slot towards right
def rslot(x, y):
    list_rslot = []
    x = x + t
    list_rslot.append((x, y))
    y = y - b
    list_rslot.append((x, y))
    x = x + e
    list_rslot.append((x, y))
    y = y + f
    list_rslot.append((x, y))
    x = x + g
    list_rslot.append((x, y))
    y = y - f
    list_rslot.append((x, y))
    x = x + e
    list_rslot.append((x, y))
    y = y - c
    list_rslot.append((x, y))
    x = x - e
    list_rslot.append((x, y))
    y = y - f
    list_rslot.append((x, y))
    x = x - g
    list_rslot.append((x, y))
    y = y + f
    list_rslot.append((x, y))
    x = x - e
    list_rslot.append((x, y))
    y = y - b
    list_rslot.append((x, y))
    x = x - t
    list_rslot.append((x, y))
    return list_rslot
#Trajectory of t slot towards up
def uslot(x, y):
    list_uslot = []
    y = y + t
    list_uslot.append((x, y))
    x = x + b
    list_uslot.append((x, y))
    y = y + e
    list_uslot.append((x, y))
    x = x - f
    list_uslot.append((x, y))
    y = y + g
    list_uslot.append((x, y))
    x = x + f
    list_uslot.append((x, y))
    y = y + e
    list_uslot.append((x, y))
    x = x + c
    list_uslot.append((x, y))
    y = y - e
    list_uslot.append((x, y))
    x = x + f
    list_uslot.append((x, y))
    y = y - g
    list_uslot.append((x, y))
    x = x - f
    list_uslot.append((x, y))
    y = y - e
    list_uslot.append((x, y))
    x = x + b
    list_uslot.append((x, y))
    y = y - t
    list_uslot.append((x, y))
    return list_uslot
#Trajectory of t slot towards down
def dslot(x, y):
    list_dslot = []
    y = y - t
    list_dslot.append((x, y))
    x = x - b
    list_dslot.append((x, y))
    y = y - e
    list_dslot.append((x, y))
    x = x + f
    list_dslot.append((x, y))
    y = y - g
    list_dslot.append((x, y))
    x = x - f
    list_dslot.append((x, y))
    y = y - e
    list_dslot.append((x, y))
    x = x - c
    list_dslot.append((x, y))
    y = y + e
    list_dslot.append((x, y))
    x = x - f
    list_dslot.append((x, y))
    y = y + g
    list_dslot.append((x, y))
    x = x + f
    list_dslot.append((x, y))
    y = y + e
    list_dslot.append((x, y))
    x = x - b
    list_dslot.append((x, y))
    y = y + t
    list_dslot.append((x, y))
    return list_dslot
#Trajectory of top and bottom sides
def topnb(x, y):
    list_top = []
    t1 = (n1 * 2 - 1) + 4 * 2
    t2 = n2 * 2 - 1
    y = y + t
    list_top.append((x, y))
    for i in range(1, 8):
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        else:
            if i == 1:
                x = x + a
            else:
                if i == 3 or i == 7:
                    x = x + b
                else:
                    x = x + c
        list_top.append((x, y))
        
    for i in range(8, t1 - 6):
        x = x + tab1 * (i % 2)
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        list_top.append((x, y))

    for i in range(t1 - 6, t1 + 1):
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        else:
            if i == t1:
                x = x + a
            else:
                if i == t1 - 6 or i == t1 - 2:
                    x = x + b
                else:
                    x = x + c
        list_top.append((x, y))
    y = y + a - t
    list_top.append((x, y))
    list_top = list_top + lslot(x, y)
    x = list_top[-1][0]
    y = list_top[-1][1]
    for i in range(5, t2 - 3):
        y = y + tab2 * (i % 2)
        if i % 2 == 0:
            x = x + t * (-1) ** (0.5 * i)
        list_top.append((x, y))
    list_top = list_top + lslot(x, y)
    x = list_top[-1][0]
    y = list_top[-1][1]
    y = y + a - t
    list_top.append((x, y))
    for i in range(1, 8):
        if i % 2 == 0:
            y = y - t * (-1) ** (0.5 * i)
        else:
            if i == 1:
                x = x - a
            else:
                if i == 3 or i == 7:
                    x = x - b
                else:
                    x = x - c
        list_top.append((x, y))
    for i in range(8, t1 - 6):
        x = x - tab1 * (i % 2)
        if i % 2 == 0:
            y = y - t * (-1) ** (0.5 * i)
        list_top.append((x, y))
    for i in range(t1 - 6, t1 + 1):
        if i % 2 == 0:
            y = y - t * (-1) ** (0.5 * i)
        else:
            if i == t1:
                x = x - a
            else:
                if i == t1 - 6 or i == t1 - 2:
                    x = x - b
                else:
                    x = x - c
        list_top.append((x, y))
    y = y - a + t
    list_top.append((x, y))
    list_top = list_top + rslot(x, y)
    x = list_top[-1][0]
    y = list_top[-1][1]
    for i in range(5, t2 - 3):
        y = y - tab2 * (i % 2)
        if i % 2 == 0:
            x = x - t * (-1) ** (0.5 * i)
        list_top.append((x, y))
    list_top = list_top + rslot(x, y)
    x = list_top[-1][0]
    y = list_top[-1][1]
    y = y - a + t
    list_top.append((x, y))
    return list_top
#Trajectory of front and back sides
def frontnb(x, y, Close):
    list_front = []
    t1 = n1 * 2 - 1
    t3 = (n3 * 2 - 1) + 4 * 2
    x = x + t
    list_front.append((x, y))
    x = x + a - t
    list_front.append((x, y))
    if Close:
        list_front = list_front + uslot(x, y)
        x = list_front[-1][0]
        y = list_front[-1][1]
        for i in range(5, t1 - 3):
            x = x + tab1 * (i % 2)
            if i % 2 == 0:
                y = y - t * (-1) ** (0.5 * i)
            list_front.append((x, y))
        list_front = list_front + uslot(x, y)
        x = list_front[-1][0]
        y = list_front[-1][1]
        x = x + a - t
        list_front.append((x, y))
    else:
        x = length * 90 - t
        list_front.append((x, y))
    for i in range(1, 8):
        if i % 2 == 0:
            x = x - t * (-1) ** (0.5 * i)
        else:
            if i == 1:
                y = y + a + t
            else:
                if i == 3 or i == 7:
                    y = y + b
                else:
                    y = y + c
        list_front.append((x, y))
    for i in range(8, t3 - 6):
        y = y + tab3 * (i % 2)
        if i % 2 == 0:
            x = x - t * (-1) ** (0.5 * i)
        list_front.append((x, y))
    for i in range(t3 - 6, t3 + 1):
        if i % 2 == 0:
            x = x - t * (-1) ** (0.5 * i)
        else:
            if i == t3:
                y = y + a + t
            else:
                if i == t3 - 6 or i == t3 - 2:
                    y = y + b
                else:
                    y = y + c
        list_front.append((x, y))
    x = x - a + t
    list_front.append((x, y))
    list_front = list_front + dslot(x, y)
    x = list_front[-1][0]
    y = list_front[-1][1]
    for i in range(5, t1 - 3):
        x = x - tab1 * (i % 2)
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        list_front.append((x, y))
    list_front = list_front + dslot(x, y)
    x = list_front[-1][0]
    y = list_front[-1][1]
    x = x - a + t
    list_front.append((x, y))
    for i in range(1, 8):
        if i % 2 == 0:
            x = x + t * (-1) ** (0.5 * i)
        else:
            if i == 1:
                y = y - a - t
            else:
                if i == 3 or i == 7:
                    y = y - b
                else:
                    y = y - c
        list_front.append((x, y))
    for i in range(8, t3 - 6):
        y = y - tab3 * (i % 2)
        if i % 2 == 0:
            x = x + t * (-1) ** (0.5 * i)
        list_front.append((x, y))
    for i in range(t3 - 6, t3 + 1):
        if i % 2 == 0:
            x = x + t * (-1) ** (0.5 * i)
        else:
            if i == t3:
                y = y - a - t
            else:
                if i == t3 - 6 or i == t3 - 2:
                    y = y - b
                else:
                    y = y - c
        list_front.append((x, y))
    return list_front
#Trajectory of left and right sides
def leftnr(x, y, Close):
    list_left = []
    t2 = (n2 * 2 - 1) + 4 * 2
    t3 = n3 * 2 - 1
    y = y + t
    list_left.append((x, y))
    for i in range(1, 8):
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        else:
            if i == 1:
                x = x + a
            else:
                if i == 3 or i == 7:
                    x = x + b
                else:
                    x = x + c
        list_left.append((x, y))
    for i in range(8, t2 - 6):
        x = x + tab2k * (i % 2)
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        list_left.append((x, y))
    for i in range(t2 - 6, t2 + 1):
        if i % 2 == 0:
            y = y + t * (-1) ** (0.5 * i)
        else:
            if i == t2:
                x = x + a
            else:
                if i == t2 - 6 or i == t2 - 2:
                    x = x + b
                else:
                    x = x + c
        list_left.append((x, y))
    y = y + a
    list_left.append((x, y))
    list_left = list_left + lslot(x, y)
    x = list_left[-1][0]
    y = list_left[-1][1]
    for i in range(5, t3 - 3):
        y = y + tab3k * (i % 2)
        if i % 2 == 0:
            x = x + t * (-1) ** (0.5 * i)
        list_left.append((x, y))
    list_left = list_left + lslot(x, y)
    x = list_left[-1][0]
    y = list_left[-1][1]
    y = y + a
    list_left.append((x, y))
    if Close:
        for i in range(1, 8):
            if i % 2 == 0:
                y = y - t * (-1) ** (0.5 * i)
            else:
                if i == 1:
                    x = x - a
                else:
                    if i == 3 or i == 7:
                        x = x - b
                    else:
                        x = x - c
            list_left.append((x, y))
        for i in range(8, t2 - 6):
            x = x - tab2k * (i % 2)
            if i % 2 == 0:
                y = y - t * (-1) ** (0.5 * i)
            list_left.append((x, y))
        for i in range(t2 - 6, t2 + 1):
            if i % 2 == 0:
                y = y - t * (-1) ** (0.5 * i)
            else:
                if i == t2:
                    x = x - a
                else:
                    if i == t2 - 6 or i == t2 - 2:
                        x = x - b
                    else:
                        x = x - c
            list_left.append((x, y))
    else:
        y = y + t
        list_left.append((x, y))
        x = x - width * 90
        list_left.append((x, y))
        y = y - t
        list_left.append((x, y))
    y = y - a
    list_left.append((x, y))
    list_left = list_left + rslot(x, y)
    x = list_left[-1][0]
    y = list_left[-1][1]
    for i in range(5, t3 - 3):
        y = y - tab3k * (i % 2)
        if i % 2 == 0:
            x = x - t * (-1) ** (0.5 * i)
        list_left.append((x, y))
    list_left = list_left + rslot(x, y)
    x = list_left[-1][0]
    y = list_left[-1][1]
    y = y - a
    list_left.append((x, y))
    return list_left

#Initialize svg file
plan = open(loc + "1.txt","w")
plan.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" ')
#Initialize 2nd svg file if the plan dosen't fit in one sheet
if 2 * length + width <= 11 and 2 * height <= 11:
    sizex = 2 * length + width + 2 * kerf + 0.5
    viewx = sizex * 90
    sizey = 2 * height + 4 * kerf + 0.5
    viewy = sizey * 90
else:
    sizex = 2 * length + 0.5
    viewx = sizex * 90
    sizey = height + width + 0.5
    viewy = sizey * 90
    plan2 = open(loc + "2.txt","w")
    plan2.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" ')
    sizex2 = 2 * width + 4 * kerf + 0.5
    viewx2 = sizex2 * 90
    sizey2 = height + 2 * kerf + 0.5
    viewy2 = sizey2 * 90
    plan2.write('width="' + str(sizex2) + 'in" height="' + str(sizey2) + 'in" viewBox = " 0 0 ' + str(viewx2) + ' ' + str(viewy2) + '" >\n')
    plan.write('width="' + str(sizex) + 'in" height="' + str(sizey) + 'in" viewBox = " 0 0 ' + str(viewx) + ' ' + str(viewy) + '" >\n')

#Define cut line style
cutstyle = '<polygon style="stroke:red; fill:none; stroke-width:0.9" points="'
#Auto-choose engrave pattern
dice = False
butterfly = False
tree = False
flower = False

if length == width == height <= 3.8 and length >= 3.0 and Close:
    dice = True
    s = length * 90
    r = str(s / 20)
    dicestyle = '" r="' + r + '" style="stroke:black;stroke-width:0.9;fill:black"/>\n'
else:
    if width >= 4 and height >= 6:
        butterfly = True
        tree = True
if not Close:
    flower = True
linestyle = '<polygon style="stroke:black; fill:none; stroke-width:0.9" points="'
dotstyle = '" r="0.9" style="stroke:black;stroke-width:0.9;fill:black"/>'

#Define patterns
#Use width and height to place butterflies and flowers
def engrave_butterfly(width, height):
    a = np.arange(-np.pi, np.pi , np.pi/1000.0)
    b = -3.0 * np.cos(2.0 * a) + np.sin(7.0 * a)- 1.0
    x = b * np.cos(a)
    y = b * np.sin(a)
    
    rot = -np.pi / 4.0
    u = 16 * (x * np.cos(rot) - y * np.sin(rot)) + width * 30
    v = 16 * (y * np.cos(rot) + x * np.sin(rot)) + height * 45
    b1 = list(zip(u, v))
    path1 = linestyle + (" ".join(str(i)[1:-1] for i in b1)) + '"/>\n'
    
    rot_1 = np.pi / 6.0
    u_1 = 10 * (x * np.cos(rot_1) - y * np.sin(rot_1)) + width * 65
    v_1 = 10 * (y * np.cos(rot_1) + x * np.sin(rot_1)) + height * 45
    b2 = list(zip(u_1, v_1))
    path2 = linestyle + (" ".join(str(i)[1:-1] for i in b2)) + '"/>\n'
    
    n_1 = 5.0
    m1 = 16 * (np.cos(n_1 * a) * np.cos(a)) + width * 40
    n1 = 16 * (np.cos(n_1 * a) * np.sin(a)) + height * 55
    f1 = list(zip(m1, n1))
    path3 = linestyle + (" ".join(str(i)[1:-1] for i in f1)) + '"/>\n'
    n_2 = 2.0
    m2 = 10 * (np.cos(n_2 * a) * np.cos(a)) + width * 45
    n2 = 10 * (np.cos(n_2 * a) * np.sin(a)) + height * 45
    f2 = list(zip(m2, n2))
    path4 = linestyle + (" ".join(str(i)[1:-1] for i in f2)) + '"/>\n'
                        
    n_3 = 3.0
    m3 = 16 * (np.cos(n_3 * a) * np.cos(a)) + width * 55
    n3 = 16 * (np.cos(n_3 * a) * np.sin(a)) + height * 55
    f3 = list(zip(m3, n3))
    path5 = linestyle + (" ".join(str(i)[1:-1] for i in f3)) + '"/>\n'
    
    path = path1 + path2 + path3 + path4 + path5
    return path
#Use length and width to place concentric flowers
def engrave_flower(length, width):
    a = np.arange(-np.pi, np.pi , np.pi / 1000.0)
    n = 5
    f = [[] for i in range(n)]
    p = [[] for i in range(n)]
    path = ''
    for i in range(0, n):
        x = (i * np.cos(n * a) * np.cos(a)) * 20 + length * 45
        y = (i * np.cos(n * a) * np.sin(a)) * 20 + width * 45
        f[i] = f[i] + list(zip(x, y))
    for i in range(0, n):
        p[i] = linestyle + (" ".join(str(j)[1:-1] for j in f[i])) + '"/>\n'
        path = path + p[i]
    return path
#Use width and height to place tree
def engrave_tree(width, height):
    a = np.array([[0.03, 0, 0, 0.45, 0, 0, 0.05], [-0.03, 0, 0, -0.45, 0, 0.4, 0.15], [0.56, -0.56, 0.56, 0.56, 0, 0.4, 0.4], [0.56, 0.56, -0.56, 0.56, 0, 0.4, 0.4]])
    x0 = 1
    y0 = 1
    m = []
    n = []
    path = ''
    for i in range(1,10000):
        r = np.random.uniform(0, 1)
        if r <= 0.05:
            x1 = a[0, 0] * x0 + a[0, 1] * y0 + a[0, 4]
            y1 = a[0, 2] * x0 + a[0, 3] * y0 + a[0, 5]
        elif 0.05 < r <= 0.2:
            x1 = a[1, 0] * x0 + a[1, 1] * y0 + a[1, 4]
            y1 = a[1, 2] * x0 + a[1, 3] * y0 + a[1, 5]
        
        elif 0.2 < r <= 0.6 :
            x1 = a[2, 0] * x0 + a[2, 1] * y0 + a[2, 4]
            y1 = a[2, 2] * x0 + a[2, 3] * y0 + a[2, 5]
        else:
            x1 = a[3, 0] * x0 + a[3, 1] * y0 + a[3, 4]
            y1 = a[3, 2] * x0 + a[3, 3] * y0 + a[3, 5]
        m.append(x1 * width * 20 + width * 45)
        n.append(y1 * height * 20 + height * 32)
        x0 = x1
        y0 = y1
    dots = list(zip(m,n))
    
    for d in dots:
        cx = d[0]
        cy = d[1]
        p = '<circle cx="' + str(cx) + '" cy="' + str(cy) + dotstyle + '\n'
        path = path + p
    return path

#Front
gx = t * 2
gy = t * 2
plan.write('<!--Front-->\n')
gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in frontnb(0, 0, Close))) + '"/>\n')
if dice:
    plan.write('<circle cx="' + str(0.5 * s) + '" cy="' + str(0.5 * s) + dicestyle)
plan.write('</g>\n')

#Back
gx = gx + length * 90
plan.write('<!--Back-->\n')
gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in frontnb(0, 0, Close))) + '"/>\n')
if dice:
    plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 4) + dicestyle)
    plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 2) + dicestyle)
    plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 4 * 3) + dicestyle)
    plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 4) + dicestyle)
    plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 2) + dicestyle)
    plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 4 * 3) + dicestyle)
plan.write('</g>\n')
#Top
if Close:
    gx = t * 2
    gy = gy + height * 90
    plan.write('<!--Top-->\n')
    gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
    plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in topnb(0, 0))) + '"/>\n')
    if dice:
        plan.write('<circle cx="' + str(s / 4) + '" cy="' + str(s / 4 * 3) + dicestyle)
        plan.write('<circle cx="' + str(s / 2) + '" cy="' + str(s / 2) + dicestyle)
        plan.write('<circle cx="' + str(s / 4 * 3) + '" cy="' + str(s / 4) + dicestyle)
        plan.write('</g>\n')
    else:
        pass

#Bottom
if Close:
    gx = gx + length * 90
else:
    gx = t * 2
    gy = gy + height * 90
plan.write('<!--Bottom-->\n')
gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in topnb(0, 0))) + '"/>\n')
if dice:
    plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 3 * 2) + dicestyle)
    plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 3) + dicestyle)
    plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 3) + dicestyle)
    plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 3 * 2) + dicestyle)
if flower:
    plan.write(engrave_flower(length, width))
plan.write('</g>\n')

#If the plan fit in one sheet
if 2 * length + width <= 11 and 2 * height <= 11:
    #left
    gx = gx + length * 90
    gy = t * 2
    plan.write('<!--Left-->\n')
    gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
    plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in leftnr(0, 0, Close))) + '"/>\n')
    if dice:
        plan.write('<circle cx="' + str(s / 3) + '" cy="' + str(s / 3 * 2) + dicestyle)
        plan.write('<circle cx="' + str(s / 3 * 2) + '" cy="' + str(s / 3) + dicestyle)
    plan.write('</g>\n')
#Right
    gy = gy + height * 90 + 2 * kerf * 90
    plan.write('<!--Right-->\n')
    gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
    plan.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in leftnr(0, 0, Close))) + '"/>\n')
    if dice:
        plan.write('<circle cx="' + str(s / 4) + '" cy="' + str(s / 4 * 3) + dicestyle)
        plan.write('<circle cx="' + str(s / 2) + '" cy="' + str(s / 2) + dicestyle)
        plan.write('<circle cx="' + str(s / 4 * 3) + '" cy="' + str(s / 4) + dicestyle)
        plan.write('<circle cx="' + str(s / 4) + '" cy="' + str(s / 4) + dicestyle)
        plan.write('<circle cx="' + str(s / 4 * 3) + '" cy="' + str(s / 4 * 3) + dicestyle)
    plan.write('</g>\n')
#If the plan doesn't fit in one sheet
else:
    #left
    gx = t * 2
    gy = t * 2
    plan2.write('<!--Left-->\n')
    gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
    plan2.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in leftnr(0, 0, Close))) + '"/>\n')
    if butterfly:
        plan2.write(engrave_butterfly(width, height))
        plan2.write('</g>\n')
    #Right
    gx = t * 2 + width * 90 + 2 * kerf * 90
    plan2.write('<!--Right-->\n')
    gtransform = '<g transform="translate(' + str(gx) + ', ' + str(gy) + ') " >\n'
    plan2.write(gtransform + cutstyle + (" ".join(str(i)[1:-1] for i in leftnr(0, 0, Close))) + '"/>\n')
    if tree:
        plan2.write(engrave_tree(width, height))
    plan2.write('</g>\n')
    #close plan 2
    plan2.write('</svg>')
    plan2.close
#Closing
plan.write('</svg>')
plan.close
print 'finished'