class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            bal = target-numbers[i]
            if bal in numbers:
                return [i+1,numbers.index(bal)+1]