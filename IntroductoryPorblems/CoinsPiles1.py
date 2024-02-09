def can_empty_piles(a, b):
    return (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b)

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        result = can_empty_piles(a, b)
        print("YES" if result else "NO")

if __name__ == "__main__":
    main()
