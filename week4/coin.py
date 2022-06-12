'''L =[1.0,2.0,3.0,4.0,5.0]
def get_range(L) :
    print(max(L) - min(L))


def max(l) :
    max = l[0]
    for i in range(len(l)) :
        if max > l[i] :
            max = l[i]
    return max


def min(l) :
    min = l[0]
    for i in range(len(l)) :
        if min < l :
            min = l[i]
    return min
get_range(L)'''

'''def asend(l):
    x = []
    print(x)
    mini = l[0]
    for i in range(len(l)):
        if mini >l[i]:
            mini= l[i]
        x.append(mini)


    return mini



print(asend([5,35,654,68,648]))'''




#i want to print sum of all natural number
'''n = int(input())
sum = 0
for i in range(0,n+1):
    sum =  sum+i
print(sum)'''




'''def sum(n):# this programe for sum of positive number
    ans = 0
    for  i in range(n+1):
        ans = ans+i
    return ans
print(sum(5))'''

'''def some_function(word):
    space = ' ' # there is a single space between the quotes
    if space in word:
        return False
    # both letters 'A' and 'Z' are in upper case
    if not('A' <= word[0] <= 'Z'):
        return False
    for i in range(1, len(word)):
        # both letters 'a' and 'z' are in lower case
        if not('a' <= word[i] <= 'z'):
            return False
    return True


print(some_function('Riemann'))'''


'''def minmax(a, b):
    if a <= b:
        return a, b
    return b, a
print(minmax(2,1))'''
'''def unique(L):
    L_uniq = [L[0]]
    for i in range(1, len(L)):
        if not(L[i] in L[:i]):
            L_uniq.append(L[i])
    return L_uniq
l = [1,1,3,54,58,4531,221,12,3,3]
print(unique(l))'''
'''L = int(input())
def mini(L):
    mini = [0]
    for i in range(L):
        if mini > i :
            mini =i
            mini.app
    return L
print(mini(L))
def asend(l):
    x = []
    print(x)
    mini = l[0]
    for i in range(len(l)):
        if mini >l[i]:
            mini= l[i]
        x.append(mini)


    return mini'''


'''def distance(word_1, word_2) :
    sum = 0

    if (len(word_1) != len(word_2)) :
        return (-1)
    else :
        for i in range(len(word_1)) :
            if (ord(word_1[i] > ord(word_2[i]))) :

                sum = sum + (ord(word_1[i]) - ord(word_2[i]))
            else :
                sum = sum+(ord(word_2[i])-ord(word_1[i]))
    return sum'''
'''def transpose(mat):

    mat_transpose = []
    row=len(mat)
    column = len(mat[0])
    for i in range (column):
        x=[]
        for j in range(row):
            x.append(mat[j][i])
        mat_transpose.append(x)
        x=[]
    return mat_transpose'''









# matrix muliplication
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
a = []
b = []
a.append(l1)
a.append(l2)
a.append(l3)
l4=[9,8,7]
l5 = [6,5,4]
l6 = [3,2,1]
b.append(l4)
b.append(l5)
b.append(l6)
'''print(b)
print(a)'''
print(a)
print(b)

















