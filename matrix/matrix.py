class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.rows = []
        self.columns = []
        self.convert(rows)

    def convert(self, rows):
        for row in rows:
            elements = row.split(' ')
            row = []

            if len(self.columns) == 0:
                [self.columns.append([]) for i in elements]

            column_num = 0

            for element in elements:
                element = int(element)
                row.append(element)
                self.columns[column_num].append(element)
                column_num += 1
            self.rows.append(row)

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
