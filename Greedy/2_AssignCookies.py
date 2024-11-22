class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      cnt=0
      i=0
      j=0
      while(j<=len(s)):
        if s[j]>=g[i]:
          cnt+=1
          i+=1
        j+=1
      return cnt