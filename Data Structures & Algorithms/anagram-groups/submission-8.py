from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        added = []
        res = dict()
        for i in strs:
            counter_obj = Counter(i)
            key = frozenset(counter_obj.items())
            if key not in res:
                res[key] = [i]
            else :
                new_val = res[key]
                new_val.append(i)
                res[key] =  new_val

        return list(res.values())

