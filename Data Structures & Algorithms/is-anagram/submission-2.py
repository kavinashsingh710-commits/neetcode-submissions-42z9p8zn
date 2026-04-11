from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = Counter(s)
        second = Counter(t)
        if first == second :
            return True
        else :
            return False
        