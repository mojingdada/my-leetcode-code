from itertools import combinations
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

