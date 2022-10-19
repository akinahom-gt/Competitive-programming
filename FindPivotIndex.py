class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    totalSum = sum(nums) 
    right=totalSum
    left=0
    
    for i in range(len(nums)):
      number=nums[i]
      right-=number
      if left==right:
    return i
      left+=number
    return -1
