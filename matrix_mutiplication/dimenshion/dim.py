# this function for intialize
def dim_instl(dim) :
    c = []
    for i in range(dim) :
        c.append([])
    for j in range(dim) :
        for k in range(dim) :
            c[k].append(0)
    return c



