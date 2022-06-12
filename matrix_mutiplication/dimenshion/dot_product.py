def dim_instl(dim) :
    c = []
    for i in range(dim) :
        c.append([])
    for j in range(dim) :
        for k in range(dim) :
            c[k].append(0)
    return c
def dot_product(u, v) :
    dim = len(u)
    ans = 0

    for i in range(dim) :
        ans = ans + u[i] * v[i]
    return ans


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


def row(M,i):
    dim = len(M)
    l =[]
    for j in range(dim):
        l.append(M[i][j])
    return l

def cloum(M,k):
    dim= len(M)
    l = []
    for i in range(dim):
        l.append(M[i][k])
    return l
def cal(A,B):
    dim = len(A)
    c =dim_instl(dim)
    for i in range(dim):
        for j in range(dim):

           c[i][j] = dot_product(row(A, i), cloum(B, j))
    return c
print(cal(x, y))