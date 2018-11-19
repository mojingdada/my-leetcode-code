class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max=0
        sum=0
        lenth=len(nums)
        for i in nums[0:k]:
            sum+=i
            max+=i
        for j in range(k,lenth):
            sum=sum+nums[j]-nums[j-k]
            if(sum>max):
                max=sum
        MaxVerage=max*1.0/k
        return MaxVerage

    if __name__ == '__main__':
        nums=[1,12,-5,-6,50,3]
        k=4
        l=findMaxAverage(nums,nums,k)
        print(l)