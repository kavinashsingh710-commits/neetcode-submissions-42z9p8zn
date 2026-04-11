class Solution:

    def rowChecks(self,board):
        for i in range(9):
            temp = []
            for j in board[i]:
                if j in temp and j != '.':
                    print("Check Failed")
                    return False
                temp.append(j)
        return True

    def colCheck(self,board):
        board = [list(row) for row in zip(*board)]
        return self.rowChecks(board)

    def dupCheck(self,board):
        box_maps={}
        for r in range(9):
            for c in range(9):
                box_index = (r // 3) * 3 + (c // 3)
                if box_index in box_maps.keys():
                    if board[r][c] not in box_maps[box_index] and board[r][c] != '.':
                        val = box_maps[box_index]
                        val.append(board[r][c])
                        box_maps[box_index] =val
                    elif board[r][c] == '.':
                        continue               
                    else:
                        print(f"Value {board[r][c]} already in {box_maps[box_index]}")
                        return False
                else:
                    box_maps[box_index] = [(board[r][c])]
        return True
                    

    def isValidSudoku(self, board) -> bool:
        if not self.rowChecks(board):
            return False
        if not self.colCheck(board):
            return False
        if not self.dupCheck(board):
            return False
        return True