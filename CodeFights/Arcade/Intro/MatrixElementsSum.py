class MatrixElementsSum:
    def __init__(self,matrix):
        self.matrix = matrix

    def matrix_elements_sum(self):
        column_remove = []
        rows = len(self.matrix)
        total = 0
        for i in range(0, rows):
            cols = len(self.matrix[i])
            for j in range(0, cols):
                if self.matrix[i][j] == 0 or j in column_remove:
                    column_remove.append(j)
                    continue
                else:
                    total = total + self.matrix[i][j]
        return total

    @staticmethod
    def get_matrix():
        print("Enter number of rows :")
        n = int(input())
        print("Enter elements")
        return [[int(j) for j in input().split()] for i in range(n)]


if __name__ == '__main__':
    matrix= MatrixElementsSum.get_matrix()
    print("Matrix: ", matrix)
    matrixElementsSum = MatrixElementsSum(matrix)
    print(matrixElementsSum.matrix_elements_sum())

