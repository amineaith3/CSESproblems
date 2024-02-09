def count_trailing_zeros_in_factorial(n):
    count = 0

    power_of_5 = 5
    while n // power_of_5 > 0:
        count += n // power_of_5
        power_of_5 *= 5

    return count

def main():
    n = int(input())
    result = count_trailing_zeros_in_factorial(n)
    print(result)

if __name__ == "__main__":
    main()
