
def tronca(l):
    del l[0]
    del l[-1]
        
    

print(tronca([1,2,3,4]))

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    """
    del t[0]
    del t[-1]

print(chop([1,2,3,4]))
