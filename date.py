# -*- coding: utf-8 -*-

def date(g,m,a):
    bis = bisestile(a)
    
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 9 or m == 10 or m == 12:
        if g > 31 and g < 1:
            return False
        else:
            return True, bis
    elif m == 11 or m == 4 or m == 6 or m == 8:
        if g > 30 and g < 1:
            return False
        else:
            return True, bis
    elif m == 2:
        if g > 28 and g < 1:
            return False
        else:
            return True, bis
    else:
        return False
    
    
def bisestile(anno):
    
    if anno % 4 == 0 and anno % 400 == 0 and anno % 100 == 0:
        return 'bisestile'
    else:
        return 'non bisestile'
    
date(11, 5, 2000)

def date2(g,m,a):
    bis = bisestile2(a)
    if m  in  (1,3,5,7,9,10,12):
        if g > 31 and g < 1:
            return False
        else:
            return True, bis
    elif m in (11,4,6,8):
        if g > 30 and g < 1:
            return False
        else:
            return True, bis
    elif m == 2:
        if g > 28 and g < 1:
            return False
        else:
            return True, bis
    else:
        return False
    
    
def bisestile2(anno):
    if anno % 400 == 0 or anno % 4 == 0 and anno % 100 != 0:
        return 'bisestile'
    else:
        return 'non bisestile'
print(date2(11, 5, 2000))


