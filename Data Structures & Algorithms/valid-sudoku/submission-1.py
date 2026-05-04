class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for i in range(0, len(board)):
            nineSet = set()
            for j in range(0, len(board[i])):
                if board[i][j] in nineSet:
                    print('1st')
                    return False
                if board[i][j] != '.':
                    nineSet.add(board[i][j])

        # columns
        for i in range(0, len(board[0])):
            nineSet = set()
            for j in range(0, len(board)):
                if board[j][i] in nineSet:
                    print('2nd')
                    return False
                if board[j][i] != '.':
                    nineSet.add(board[j][i])
        
        # squares
        # treat as 3 x 3 matrices
        for i in range(0, 3):
            for j in range(0, 3):
                nineSet = set()
                for k in range(0, 3):
                    for q in range(0, 3):
                        if board[k+(i*3)][q+(j*3)] in nineSet:
                            print('3rd')
                            return False
                        if board[k+(i*3)][q+(j*3)] != '.':
                            nineSet.add(board[k+(i*3)][q+(j*3)])
        return True