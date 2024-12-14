MATRIX = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

def transpose(matrix: list[list]) -> list[list]:
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix


print(transpose(MATRIX))