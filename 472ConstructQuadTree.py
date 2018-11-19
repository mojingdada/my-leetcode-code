
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if(isLeaf(grid)==True):
            node=Node(True, True, None, None, None, None)
        elif(isLeaf(grid)==False):
            node=Node(False, True, None, None, None, None)
        else:
            len1=len(grid)//2
            topLeft=[[grid[i][j]for j in range(len1)] for i in range(len1)]
            topRight = [[grid[i][j] for j in range(len1,len(grid))]for i in range(len1)]
            bottomLeft = [[grid[i][j] for j in range(len1)]for i in range(len1,len(grid))]
            bottomRight = [[grid[i][j] for j in range(len1,len(grid))] for i in range(len1,len(grid))]
            node=Node(True,False,self.construct(topLeft),self.construct(topRight),self.construct(bottomLeft),self.construct(bottomRight))
        return node

def isLeaf(grid):
    _len=len(grid)
    _sum=0
    for i in range(_len):
        _sum=sum(grid[i])+_sum
    if (_sum==_len**2):
        return True
    elif(_sum==0):
        return False
    else:
        return 11




if __name__ == '__main__':
    solution=Solution()
    grid=[[1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0]]
    print(solution.construct(grid))



