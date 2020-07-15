class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in line.split()] for line in matrix_string.splitlines()]


    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))][index-1]
