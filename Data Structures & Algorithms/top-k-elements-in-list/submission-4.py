from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #temp = "".join(str(x) for x in nums)
        final = []
        nums_dict = Counter(nums)
        print(nums_dict)
        for i in nums_dict.most_common(k):
            final.append(int(i[0]))
        return final

