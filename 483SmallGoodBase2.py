import math
class Solution(object):
    def smallgoodbase(self,n):
        j=math.log(n,2)
        for l in range(int(j),1,-1):
            m=find(n,l)
            if(m!=0):
               return m
        return str(n-1)

def find(n,i):
    ll=2
    lr=int(math.pow(n,1/i))
    while(lr>=ll):
        sum = 0
        t = 1
        mid=int((ll+lr+1)/2)
        for j in range(1,i+2):
          sum=sum+t
          t=t*mid
        if (sum ==n):
          return mid
        elif(sum<n):
           ll=mid+1
        elif(sum>n):
            lr=mid-1
    return 0

if __name__ == '__main__':
    n = input("n=")
    l = Solution.smallgoodbase(int(n),int(n))
    print(l)
