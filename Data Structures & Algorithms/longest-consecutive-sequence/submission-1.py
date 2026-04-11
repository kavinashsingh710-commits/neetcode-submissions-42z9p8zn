class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = list(set(nums))
            nums.sort()
            max_len = 0
            res = 0
            for i in range(len(nums)-1):
                if nums[i]+1 == nums[i+1]:
                    max_len =  max_len + 1
                    if max_len > res:
                        res = max_len
                else :
                    max_len = 0
            return res+1
        else:
            return 0
