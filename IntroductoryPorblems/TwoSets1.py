def find_subarray_with_sum(arr, x):
    current_sum, start = arr[0], 0

    for end in range(1, len(arr) + 1):
        while current_sum > x and start < end - 1:
            current_sum -= arr[start]
            start += 1

        if current_sum == x:
            return arr[start:end]

        if end < len(arr):
            current_sum += arr[end]

    return None

def main():
    n = int(input())
    arr = list(range(1, n + 1))
    s = n * (n + 1) // 2

    if s % 2 == 0:
        new_data = find_subarray_with_sum(arr, s // 2)
        if new_data:
            print("YES")
            print(len(new_data))
            print(" ".join(map(str, new_data)))
            
            to_remove_set = set(new_data)
            remaining_data = [data for data in arr if data not in to_remove_set]

            print(len(remaining_data))
            print(" ".join(map(str, remaining_data)))
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()
