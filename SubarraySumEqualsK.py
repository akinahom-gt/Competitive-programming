class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        count[0] = 1
        ans = preS = 0
        for num in nums:
            preS += num
            ans += count[preS - k]
            count[preS] +=1
        return ans
