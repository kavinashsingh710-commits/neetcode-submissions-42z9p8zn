class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for st in strs:
            res = res + str(len(st)) +'#'+ st
        return res

    def decode(self, s: str) -> List[str]:
        final = []
        i=0
        while i < len(s):
            j=i
            while s[j]!= '#':
                j=j+1
            print(s[i:j])
            length = int(s[i:j])
            i = j + 1 + length
            final.append(s[j+1:j+1+length])
        return final