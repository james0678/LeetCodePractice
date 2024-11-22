#https://leetcode.com/problems/array-partition/?envType=problem-list-v2&envId=greedy&difficulty=EASY

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
      answer=0
      nums.sort()
      for i in range(0,len(nums)-1, 2):
          answer+=nums[i]
      return answer