class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        ans=[]
        count=0
        for i in nums:
            for j in range(l):
               if (nums[j]-i)<0:
                   count+=1
            ans.append(count)
            count=0
        return ans
