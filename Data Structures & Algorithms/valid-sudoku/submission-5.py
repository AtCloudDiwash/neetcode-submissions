class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows for the duplicate numbers
        for row in board:
            if len(list(filter(lambda x:x.isdigit(), row))) != len(set(list(filter(lambda x:x.isdigit(), row)))):
                print("row")
                return False

        # Check cols for the duplicate numbers
        cols = [list(col) for col in list(zip(*board))]

        for col in cols:
            if len(list(filter(lambda x:x.isdigit(), col))) != len(set(list(filter(lambda x:x.isdigit(), col)))):
                print(set(list(filter(lambda x:x.isdigit(), col))))
                return False
        

        # Check the sub-matrix
        sub = [[] for _ in range(9)]
        counter, checkpoint = 0, 0
        for i in range(9):
            for j in range(0, 9, 3):
                sub[counter + checkpoint * 3].extend(filter(lambda x:x.isdigit(), board[i][j:j+3]))
                counter += 1
            counter = 0

            if i != 0 and (i+1) % 3 == 0:
                checkpoint += 1

        for item in sub:
            if len(set(item)) != len(item):
                return False
        return True

            
        

        
        
            