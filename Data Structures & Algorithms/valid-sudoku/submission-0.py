class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for row in range(9):
            nums = board[row]
            nums = [x for x in nums if x != "."]

            if len(nums) != len(set(nums)):
                return False

        # columns
        for col in range(9):
            nums = []

            for row in range(9):
                nums.append(board[row][col])

            nums = [x for x in nums if x != "."]

            if len(nums) != len(set(nums)):
                return False

        # split every row into 3-element lists
        mod_nums = []

        for row in board:
            for i in range(0, 9, 3):
                mod_nums.append(row[i:i+3])

        # check 3x3 boxes
        for row_group in range(0, 9, 3):
            for col_group in range(3):

                nums = []

                nums += mod_nums[row_group * 3 + col_group]
                nums += mod_nums[(row_group + 1) * 3 + col_group]
                nums += mod_nums[(row_group + 2) * 3 + col_group]

                nums = [x for x in nums if x != "."]

                if len(nums) != len(set(nums)):
                    return False

        return True