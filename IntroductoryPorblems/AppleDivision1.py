n = int(input())
p = list(map(int, input().split()))

ss = sum(p)
ans = 0

for i in range(1 << n):
    cs = 0
    for j in range(n):
        if i >> j & 1:
            cs += p[j]

    if cs <= ss / 2:
        ans = max(ans, cs)

result = ss - 2 * ans
print(result)
