def generate_strings(input_str, current_str, used, result):
    if len(current_str) == len(input_str):
        result.add(current_str)
        return

    for i in range(len(input_str)):
        if not used[i]:
            used[i] = True
            generate_strings(input_str, current_str + input_str[i], used, result)
            used[i] = False

def order(arr):
    return sorted(set(arr))

def main():
    input_str = input().strip()
    n = len(input_str)

    used = [False] * n
    result = set()

    generate_strings(input_str, "", used, result)
    result = order(result)

    print(len(result))
    for string in result:
        print(string)

if __name__ == "__main__":
    main()
