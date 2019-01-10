class Solution( object ):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list=[]
        for i in range(left,right+1):
            l=0
            n1=len(str(i))
            for j in range(n1):
                k=int(i/(10**j)%10)
                if(k!=0 and i%k==0):
                    continue
                else:
                    l=l+1
                    break
            if(l==0):
                list.append(i)
            else:
                continue
        return list



if __name__ == '__main__':
    s=Solution()
    list=s.selfDividingNumbers(1,22)
    print(list)

