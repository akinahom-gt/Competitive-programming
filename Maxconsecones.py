class Solution(object):
    def longestOnes(self, nums, k):
        max_, zero, ptr = 0, 0, 0
        for index, value in enumerate(nums):
            if value == 0: zero += 1
            while zero > k:
                if nums[ptr] == 0: zero -= 1
                ptr += 1
            max_ = max(max_, (index - ptr) + 1)
        return max_
