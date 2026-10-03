class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #print("matrix" , matrix)
        #print("len" , len(matrix), "len col", len(matrix[0]))
        self.matrix  = matrix

        
        
    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #print(row1, col1, row2, col2)
        top = self.matrix[row1][col1]
        bot = self.matrix[row2][col2]
        col_diff = col1 - col2 
        row_diff = row1 - row2

        total = 0 
        row = row1
        col = col1
        while row <= row2:
            col = col1 
            while col <= col2:

                total = total + self.matrix[row][col]
                col +=1
            row += 1
        return total




        

        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)