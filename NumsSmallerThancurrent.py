class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans=[]
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
               if j!=i and nums[j]< nums[i]:
                   count+=1
            ans.append(count)
            count=0
        return ans
