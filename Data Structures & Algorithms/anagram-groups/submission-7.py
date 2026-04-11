from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        added = []
        for i in range(len(strs)):
            sub_res=[]
            if i not in added:
                sub_res.append(strs[i])
                added.append(i)
                for j in range(i+1,len(strs)):
                    if Counter(strs[i]) == Counter(strs[j]):
                        if j not in added :
                            sub_res.append(strs[j])
                            added.append(j)
            if sub_res:
                result.append(sub_res)
        return result

