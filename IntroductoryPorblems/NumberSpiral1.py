tests = int(input())
data = list()
for  _ in range(tests):
    couple = tuple(map(int, input().split()))
    data.append(couple)
    
for i in range(tests):
    x, y = data[i]
    m = max(x, y)
    if m == x:
        if x % 2 == 0:
            print(x**2 - y + 1)
        else : 
            print((x-1)**2 + y)
    else : 
        if y % 2 == 1:
            print(y**2 - x + 1)
        else : 
            print((y-1)**2 + x)
