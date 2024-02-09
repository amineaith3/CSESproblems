def create_palindrome(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_chars = []
    for char, count in char_counts.items():
        if count % 2 == 1:
            odd_chars.append(char)

    if len(odd_chars) > 1:
        return "NO SOLUTION"

    first_half = ""
    for char, count in char_counts.items():
        first_half += char * (count // 2)

    center_char = odd_chars[0] if odd_chars else ""

    second_half = first_half[::-1]

    palindrome = first_half + center_char + second_half

    return palindrome

s = input().strip()
result = create_palindrome(s)
print(result)
