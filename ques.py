n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1:
            print(j)
        else:
            print(j, end=',')

    print(end='\n')