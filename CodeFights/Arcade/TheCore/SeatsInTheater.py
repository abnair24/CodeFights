# For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be
# seatsInTheater(nCols, nRows, col, row) = 96.


def seatsInTheater(nCols, nRows, col, row):
    remCols = nCols - col + 1  # include the column which he sits
    remRows = nRows - row

    return remCols * remRows
