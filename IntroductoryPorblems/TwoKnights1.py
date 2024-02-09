n = int(input())
for x in range(1, n+1):
    squares = x**2
    maxPossibles = squares * (squares - 1) // 2
    if (x > 2):
        maxPossibles -= 4 * (x - 1) * (x - 2)
    print(maxPossibles)
