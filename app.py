class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        
        rows = len(mat)
        if rows == 0:
            return []
        
        cols = len(mat[0])
        
        ret = []
        
        for i in range(rows):
            for j in range(cols):
                
                if mat[i][j] == 1:
                    if not self.check_row(rows, i, j, mat):
                        continue
                    if not self.check_col(cols, i, j, mat):
                        continue
                        
                    ret.append([i, j])
        return ret
        
    def check_row(self, row: int, i:int, j:int , mat: List[List[int]]):
        for r in range(row):
            if r == i:
                continue;

            if mat[r][j] == 1:
                return False
                    
        return True
        
        
    def check_col(self, col: int, i:int, j:int , mat: List[List[int]]):
        for c in range(row):
            if c == j:
                continue;

            if mat[i][c] == 1:
                return False
                
        return True
        