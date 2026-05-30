class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted, once nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate values for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate values for the third number
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result