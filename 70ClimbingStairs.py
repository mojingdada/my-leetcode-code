class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[0,1,2]
        if(n==1):
            return 1
        if(n==2):
            return 2
        else:
            for i in range(3,n+1):
                nums.append(nums[i-1]+nums[i-2])
        return nums[n]
    if __name__ == '__main__':
        item=climbStairs(5,5)
        print(item)

