def solve(n, src, dest, aux):
    moves = list()
    if n == 1:
        return [(src, dest)]
    moves.extend(solve(n-1, src, aux, dest))
    moves.append((src, dest))
    moves.extend(solve(n-1, aux, dest, src))
    return moves

def main():
    n = int(input())
    moves = solve(n, 1, 3, 2)

    print(len(moves))
    for move in moves:
        print(f"{move[0]} {move[1]}")

if __name__ == "__main__":
    main()
