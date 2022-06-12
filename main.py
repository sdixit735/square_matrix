# '''name = input()
# nick = ''    # there is no space between the quotes
# space = ' ' # there is one space between the quotes
# first_char = True
# for char in name:
#     if first_char == True:
#         nick = nick + char
#
#
#
#
#     if char == space:
#         first_char = True
# print(nick)'''
# '''word = input()
# valid = True
# for i in range(len(word)):
#     char = word[i]
#     if i % 2 == 0 and char not in 'aeiou':
#         valid = False
# print(valid)
# print(len(word))'''
# '''boxes = input()
# num = 0
# total = 0
# for coins in boxes:
#     total += coins
#     num += 1
# avg = total / num'''
# '''n= int(input())
# y = n+1
# add = 0
# for i in range(1,y):
#     for j in range(i):
#
#       add = add+i
#       i = i-1
#       print(i)
# print(add)'''
# '''n = int(input())
# if n > 1:
#     for i in range(2, n + 1):
#
#         if n % i == 0:
#             n = n // i
#             print(i)'''
#
# com = input()
# le = len(com)
# for i in range((le)):
#     print(i,end=',')
#
#
#
'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == j:
            print(j)
        else:
            print(j, end=',')
    if i != j:
        print(end='\n')

for i in reversed(range(1, n + 1)):
    for j in range(1, i ):
        if i -1 == j:
            print(j)

        else:
            print(j, end=',')
    if i-1 != j:
        print(end='\n')'''
'''n = input()

def bool checkFirstDigit( fname ):


match agrument:
    case 0:
        return "zero"
    case 1:
        return "one"
    case 2:
        return "two"
    case default:
        return "something"


    return switcher.get(argument, "nothing")'''
'''n = input()
b = [6,7,8,9]
c =10
coun = 0

if len(n)==c:
    for i in range(len(n)):
        if i ==1:
            if b.__contains__(i):
                n.c
                    print()'''
a= input()
b = '9876'
if a[0] in b and len(a)==10:
    count_1=0
    current_1 = None
    for j in a:
        if j == current_1:
            count_1 = count_1 +1
            if count_1 >7:
                print('invalid')
            else:
                current, count_2, max = None, 0,0
                for k in a :
                    if k == current:
                        count_2 = count_2 +1
                        if count_2>max:
                            max= count_2
                            if max>5:
                                break
                        else:
                            current = k
                            count_2 = 1
    if max > 5:
      print('invalid')
    else:
     print('valid')
else:
 print('invalid')



