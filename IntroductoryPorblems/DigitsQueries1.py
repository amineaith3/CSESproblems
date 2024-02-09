def find_digit_at_position(k):
    current_length = 1
    count_digits = 9
    start_number = 1

    while k > current_length * count_digits:
        k -= current_length * count_digits
        current_length += 1
        count_digits *= 10
        start_number *= 10

    target_number = start_number + (k - 1) // current_length

    digit_position = (k - 1) % current_length

    digit = int(str(target_number)[digit_position])

    return digit

q = int(input())
for _ in range(q):
    k = int(input())
    result = find_digit_at_position(k)
    print(result)
