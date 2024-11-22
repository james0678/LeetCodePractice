#https://leetcode.com/problems/can-place-flowers/description/?envType=problem-list-v2&envId=greedy&difficulty=EASY
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], x: int) -> bool:
        count=0
        flowerbed = [0] + flowerbed
        flowerbed.append(0)
        n=len(flowerbed)-1
        l=len(flowerbed)-2
        m=len(flowerbed)-3
        print(flowerbed)
        while(m>=0):
            if flowerbed[n] == flowerbed[l] == flowerbed[m] == 0:
              print(m,l,n)
              count+=1
              n-=2
              l-=2
              m-=2
            else:
              n-=1
              l-=1
              m-=1
        print(count)
        print(n)
        if count < x:
          return False
        else:
          return True
        
        
        

"""
Greedy Approach
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = len(flowerbed)
        bed = [0] + flowerbed + [0]
        
        for i in range(1, s+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            
            if n <= 0: return True
        
        return False
"""
