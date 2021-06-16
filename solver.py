
sudokuArr = [   [4,0,0,0,0,8,0,0,2],
                [0,0,0,7,0,0,0,0,0],
                [0,0,0,0,9,1,0,7,0],
                [0,1,0,5,0,6,0,0,0],
                [6,0,0,0,0,4,0,9,0],
                [0,5,0,0,0,0,8,0,0],
                [3,4,0,0,0,2,0,0,1],
                [8,0,0,0,3,0,0,0,6],
                [0,2,0,8,1,0,0,0,0]  ]

def printArr(arr):
    for i in arr:
        print(i)
    print("\n")

def sudokuFull(array):
    for i in array:
        for j in i:
            if j == 0:
                return False
    return True

def isCorrect(x,y,value):
    newSudoku = sudokuArr.copy()
    newSudoku[y][x] = value
    
    row = newSudoku[y].copy()
    del row[x]

    column = []
    for i in newSudoku:
        column.append(i[x])
    del column[y]

    box = []
    startCol = x - x % 3
    startRow = y - y % 3
    for i in range(3):
        for j in range(3):
            box.append(newSudoku[startRow+i][startCol+j])
    del box[3*(y%3)+(x%3)]

    if newSudoku[y][x] in row:
        return False
    elif newSudoku[y][x] in column:
        return False
    elif newSudoku[y][x] in box:
        return False
    else:
        return True

def solveSudoku(sudokuArr):
    for i in range(0,81):
        y=i//9
        x=i%9
        if sudokuArr[y][x] == 0:
            for value in range (1,10):
                if isCorrect(x,y,value):
                    sudokuArr[y][x]=value
                    if sudokuFull(sudokuArr):
                        print("Grid Complete and Checked")
                        return True
                    else:
                        if solveSudoku(sudokuArr):
                            return True
            break
    sudokuArr[y][x]=0

def main():
    if(solveSudoku(sudokuArr)):
        printArr(sudokuArr)
    
if __name__ == "__main__":
    main()