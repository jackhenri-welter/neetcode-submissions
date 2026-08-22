class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashmap = {}
            for j in range(9):
                if(board[i][j] == '.'):
                    continue
                if hashmap.get(board[i][j]) != None:
                    print(f"Case 1, {i}")
                    return False
                else:
                    hashmap[board[i][j]] = 0
        for i in range(9):
            hashmap = {}
            for j in range(9):
                if(board[j][i] == '.'):
                    continue
                if hashmap.get(board[j][i]) != None:
                    print("Case 2")
                    return False
                else:
                    hashmap[board[j][i]] = 0
        for i in range(3):
            for j in range(3):
                hashmap = {}
                for k in range(3):
                    for l in range(3):
                        if(board[i * 3 + k][j * 3 + l] == '.'):
                            continue
                        if hashmap.get(board[i * 3 + k][j * 3 + l]) != None:
                            print("Case 3")
                            return False
                        else:
                            hashmap[board[i * 3 + k][j * 3 + l]] = 0
        return True


        

        