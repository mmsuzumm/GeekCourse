class Matrix:
    def __init__(self, data_lst):
        self.data_lst = data_lst

    def __str__(self):
        return '\n'.join(' '.join(map(str, line)) for line in self.data_lst)

    def __add__(self, other):
        final_matrix = []
        if len(self.data_lst) == len(other.data_lst):
            for line_one, line_two in zip(self.data_lst, other.data_lst):
                if len(line_one) != len(line_two):
                    return 'Error 1'
                final_line = [x + y for x, y in zip(line_one, line_two)]
                final_matrix.append(final_line)
        else:
            return 'Error 2'
        return Matrix(final_matrix)


matrix_one = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_test = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_test_two = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_two = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_three = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix_one)
print('...................')
print(matrix_one + matrix_test + matrix_test_two)
