class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums//rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
            return self.nums - other.nums
        else:
            return 'Второе значение больше'

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __floordiv__(self, other):
        pass  # что надо было сделать с __floordiv__?

    def __truediv__(self, other):
        return str(round(self.nums/ other.nums))


cell_one = Cell(15)
cell_two = Cell(22)
print(cell_one)
print(cell_one + cell_two)
print(cell_two.make_order(21))