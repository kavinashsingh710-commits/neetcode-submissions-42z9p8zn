class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            temp = nums.copy()
            print(i)
            print(temp)
            temp.pop(i)
            for item in temp :
                product = product * item
            result.append(product)
        return result