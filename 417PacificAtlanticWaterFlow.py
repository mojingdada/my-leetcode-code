class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m,n=len(matrix),len(matrix[0])
        p_visted=[[False]*n for _ in range(m)]
        a_visted=[[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(p_visted,matrix,m,n,i,0)
            self.dfs(a_visted,matrix,m,n,i,n-1)
        for j in range(n):
            self.dfs(p_visted,matrix,m,n,0,j)
            self.dfs(a_visted,matrix,m,n,m-1,j)
        res=[]
        for i in range(m):
            for j in range(n):
                if (p_visted[i][j] and a_visted[i][j]):
                     res.append([i,j])
        return res
    def dfs(self,visited,matrix,m,n,i,j):
        visited[i][j]=True
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        for dire in directions:
            x,y=i+dire[0],j+dire[1]
            if (x<0 or x>=m or y<0 or y>=n or matrix[x][y]<=matrix[i][j] or visited[x][y]):
                continue
            self.dfs(visited,matrix,m,n,x,y)


if __name__ == '__main__':
    matrix=[[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]]
    # matrix=[[1,1],[1,1],[1,1]]
    pacificAtlantic=Solution()
    print(pacificAtlantic.pacificAtlantic(matrix))
    # Solution.pacificAtlantic(self,matrix)


