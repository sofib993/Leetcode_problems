class Solution:    
    def findUnion(self, a, b):
        a = set(a)
        b = set(b)
        
        result = a | b
        return list(result)
