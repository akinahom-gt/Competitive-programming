class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        p = 1
        # left
        for i, num in enumerate(nums):
            res[i] = p
            p *= num

        p = 1

        for i, num in reversed(list(enumerate(nums))): # i is also reversed
            res[i] *= p
            p *= num

        return res
