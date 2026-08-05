class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # collect sub-matrix
        res = []
        res_sub_dict = []
        for row in range(0, len(board), 3):
            for col in range(0, len(board[row]), 3):
                res_sub = []
                res_sub.extend(x for x in board[row][col:col+3] if x != ".")
                res_sub.extend(x for x in board[row+1][col:col+3] if x != ".")
                res_sub.extend(x for x in board[row+2][col:col+3] if x != ".")
                res.append(res_sub)
        
        for item in res:
            dupli = {}
            for num in item:
                if num in dupli:
                    # Checking first condition: if the sub-matrix has repeating number
                    return False
                else:
                    dupli[num] = 1
            res_sub_dict.append(dupli)
        print(res_sub_dict)

        # Checking second condition: if the rows are same
        cond_2_arr = []
        for row in board:
            cond_2_arr.append(row)

        cond_2_arr2 = [list(col) for col in zip(*board)]
        def valid(group):
            nums = [x for x in group if x != "."]
            return len(nums) == len(set(nums))
        
        for row in cond_2_arr:
            if not valid(row):
                return False

        for col in cond_2_arr2:
            if not valid(col):
                return False
        
        return True




        
        
            

                

                
                


            
        
