class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        frst = strs[0]

        for i in range(len(frst)):
            word = frst[i]
            for other in strs[1:]:
                if i >= len(other) or other[i] != word:
                    return frst[:i]
        
        return frst
