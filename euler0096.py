#!/usr/bin/python
"""Su Doku

   Su Doku (Japanese meaning *number place*) is the name given to a popular
   puzzle concept.  Its origin is unclear, but credit must be attributed to
   Leonhard Euler who invented a similar, and much more difficult, puzzle idea
   called Latin Squares.  The objective of Su Doku puzzles, however, is to
   replace the blanks (or zeros) in a 9 by 9 grid in such that each row,
   column, and 3 by 3 box contains each of the digits 1 to 9.  Below is an
   example of a typical starting puzzle grid and its solution grid.

       +-----+-----+-----+  +-----+-----+-----+
       |0 0 3|0 2 0|6 0 0|  |4 8 3|9 2 1|6 5 7|
       |9 0 0|3 0 5|0 0 1|  |9 6 7|3 4 5|8 2 1|
       |0 0 1|8 0 6|4 0 0|  |2 5 1|8 7 6|4 9 3|
       +-----+-----+-----+  +-----+-----+-----+
       |0 0 8|1 0 2|9 0 0|  |5 4 8|1 3 2|9 7 6|
       |7 0 0|0 0 0|0 0 8|  |7 2 9|5 6 4|1 3 8|
       |0 0 6|7 0 8|2 0 0|  |1 3 6|7 9 8|2 4 5|
       +-----+-----+-----+  +-----+-----+-----+
       |0 0 2|6 0 9|5 0 0|  |3 7 2|6 8 9|5 1 4|
       |8 0 0|2 0 3|0 0 9|  |8 1 4|2 5 3|7 6 9|
       |0 0 5|0 1 0|3 0 0|  |6 9 5|4 1 7|3 8 2|
       +-----+-----+-----+  +-----+-----+-----+


   A well constructed Su Doku puzzle has a unique solution and can be solved by
   logic, although it may be necessary to employ "guess and test" methods in
   order to eliminate options (there is much contested opinion over this).  The
   complexity of the search determines the difficulty of the puzzle; the
   example above is considered *easy* because it can be solved by straight
   forward direct deduction.

   The 6K text file, `sudoku.txt` (right click and 'Save Link/Target As...'),
   contains fifty different Su Doku puzzles ranging in difficulty, but all with
   unique solutions (the first puzzle in the file is the example above).

   By solving all fifty puzzles find the sum of the 3-digit numbers found in
   the top left corner of each solution grid; for example, 483 is the 3-digit
   number found in the top left corner of the solution grid above."""

from __future__ import with_statement

def solveSudoku(puzzle):   # `puzzle` must be a 9x9 2D list of ints.
    obstruct = [[0] * 9 for _ in xrange(9)]
    def addObs(obst, y, x):
        def obstructIf(y,x):
            if obstruct[y][x] != -1:
                obstruct[y][x] += obst
        for i in xrange(9):
            if i != x: obstructIf(y,i)
            if i != y: obstructIf(i,x)
        t1 = y % 3
        t2 = x % 3
        x0 = x - t2
        y0 = y - t1
        obstructIf(y0 + (t1 + 1) % 3, x0 + (t2 + 1) % 3)
        obstructIf(y0 + (t1 + 1) % 3, x0 + (t2 + 2) % 3)
        obstructIf(y0 + (t1 + 2) % 3, x0 + (t2 + 1) % 3)
        obstructIf(y0 + (t1 + 2) % 3, x0 + (t2 + 2) % 3)
    for i in xrange(9):
        for j in xrange(9):
            if puzzle[i][j] != 0:
                obstruct[i][j] = -1
                addObs(1 << ((puzzle[i][j] - 1) * 2), i, j)
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if obstruct[i][j] != -1:
                nextTest = puzzle[i][j]
                testMask = 3 << (nextTest * 2)
                if puzzle[i][j] != 0:
                    addObs(-(1 << ((puzzle[i][j] - 1) * 2)), i, j)
                    puzzle[i][j] = 0
                nextTest += 1
                while nextTest <= 9:
                    if (testMask & obstruct[i][j]) == 0:
                        puzzle[i][j] = nextTest
                        addObs(1 << ((nextTest - 1) * 2), i, j)
                        break
                    nextTest += 1
                    testMask <<= 2
                if nextTest > 9:
                    # Backtrack
                    while True:
                        j -= 1
                        if j < 0:
                            j = 8
                            i -= 1
                            if i < 0: raise ValueError('no solution')
                        if obstruct[i][j] != -1:
                            if obstruct[i][j] != 0x3FFFF:
                                j -= 1
                                if j < 0:
                                    j = 8
                                    i -= 1
                                break
                            addObs(-(1 << ((puzzle[i][j] - 1) * 2)), i, j)
                            puzzle[i][j] = 0
            j += 1
        i += 1

accum = 0
with open('data/sudoku.txt') as fp:
    for _ in xrange(50):
        print fp.readline().strip()
        grid = [map(int, fp.readline().strip()) for _ in xrange(9)]
        solveSudoku(grid)
        for row in grid:
            print ''.join(str(i) for i in row)
        print
        accum += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
print accum
