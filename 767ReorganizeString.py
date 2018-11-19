class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n=len(S)
        str={}
        for i in S:
          str[i]=0
        for i in S:
          str[i]=str[i]+1
        str1=sorted(str.items(),key = lambda x:x[1],reverse = True)
        if (str1[0][1] >= (n / 2) + 1):
          return ""
        else:
            key1=[]
            vaule1=[]
            for i in range(len(str1)):
                key1.append((str1[i][0]))
                vaule1.append(str1[i][1])
            str1=dict(zip(key1,vaule1))
            str2=''
            for m in range(n):
              m = m % 2
              if(len(str1)>1):
                  temp1=list(str1.keys())[m]
                  str2=str2+temp1
                  str1[temp1]=str1[temp1]-1
                  if(str1[temp1]==0):
                     str1 = sorted(str1.items(), key=lambda x: x[1], reverse=True)
                     key1 = []
                     vaule1 = []
                     for i in range(len(str1)):
                         key1.append((str1[i][0]))
                         vaule1.append(str1[i][1])
                     str1 = dict(zip(key1, vaule1))
                     str1.pop(temp1)
                  else:
                     pass
              else:
                  temp1 = list(str1.keys())[0]
                  str2 = str2 + temp1
        return str2
    if __name__ == '__main__':
         print(reorganizeString('aab','sfffp'))

