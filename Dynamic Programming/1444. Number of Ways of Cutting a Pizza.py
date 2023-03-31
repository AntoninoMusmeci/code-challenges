#https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/?orderBy=most_votes
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        apples_col = {}
        apples_row = {}
        
        @cache
        def cut(startr,endr,startc,endc,k):
            result = 0
            if k == 0:
                return 1
            for i in range(startr+1,endr):
                if(mat[startr][startc] - mat[i][startc] > 0 and mat[i][startc] > 0):  
                   result+= cut(i,endr,startc,endc, k - 1)
            
            for j in range(startc+1,endc):
                if(mat[startr][startc]  - mat[startr][j] > 0 and mat[startr][j] > 0):
                    result+= cut(startr,endr,j,endc, k - 1)
            return result
        n = len(pizza)
        m = len(pizza[0])
        mat = [[0] * (m + 1) for i in range(n+1)]
     
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                apple = 1 if pizza[i][j] == "A" else 0
                mat[i][j] = mat[i][j+1] + mat[i + 1][j] - mat[i+1][j+1] + apple
        print(mat)


        result = cut(0,n+1,0,m+1,k-1)

        return result % (10**9 + 7)