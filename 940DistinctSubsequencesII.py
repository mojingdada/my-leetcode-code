from itertools import combinations
# class Solution:
#     def distinctSubseqII(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#         n=len(S)
#         queue=[]
#         for i in range(1,n+1):
#            queue.append(set(combinations(S,i)))
#         n1=len(queue)
#         num=0
#         for j in range(n1):
#             num+=len(queue[j])
#         return num
class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        pos, mod, cur_sum = [0]*26, 1e9+7, 1
        for c in S:
            old_sum = cur_sum
            cur_sum = (cur_sum*2 - pos[ord(c) - 97]) % mod
            pos[ord(c) - 97] = old_sum
        return cur_sum - 1




if __name__ == '__main__':
    s=Solution()
    queue1=s.distinctSubseqII('aba')
    print(queue1)

