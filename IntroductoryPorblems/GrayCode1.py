def generate_gray_code(n):
    if n == 0:
        return ['0']
    elif n == 1:
        return ['0', '1']
    else:
        prev_gray_code = generate_gray_code(n - 1)
        reflected_gray_code = prev_gray_code[::-1]
        return ['0' + code for code in prev_gray_code] + ['1' + code for code in reflected_gray_code]

def main():
    n = int(input())
    gray_code = generate_gray_code(n)
    for code in gray_code:
        print(code)

if __name__ == "__main__":
    main()
