def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
 
    result = [[0] * cols_b for _ in range(rows_a)]
 
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
 
    return result
 
def matrix_exponentiation(base_matrix, exponent):
    n = len(base_matrix)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    current_power = [row[:] for row in base_matrix]
 
    while exponent > 0:
        if exponent % 2 == 1:
            result = matrix_multiply(result, current_power)
        current_power = matrix_multiply(current_power, current_power)
        exponent //= 2
 
    return result[0][0]
 
def calculate_2_to_the_power_of_n(n):
    base_matrix = [[2]]
    result = matrix_exponentiation(base_matrix, n)
    return result % 1000000007
 
n = int(input())
result = calculate_2_to_the_power_of_n(n)
print(result)
