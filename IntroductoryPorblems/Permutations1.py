n = int(input())
answer = list()

if n == 1:
    print("1")
elif n <= 3:
    print("NO SOLUTION")
elif n == 4:
    print("2 4 1 3")
else :
    for i in range(1, n+1,2):
        answer.append(i)
    for i in range(2, n+1, 2):
        answer.append(i)
    for s in answer:
        print(f"{s} ", end="")
