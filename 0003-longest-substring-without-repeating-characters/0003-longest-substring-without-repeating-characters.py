class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range(n):
            a=set()
            for j in range(i,n):
                if s[j] in a:
                    break
                else:
                    a.add(s[j])
                    res=max(res,j-i+1)
        return res