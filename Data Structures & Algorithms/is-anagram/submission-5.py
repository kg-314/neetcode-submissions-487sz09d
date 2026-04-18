class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}

        for i in s:
            freqs[i] = freqs.get(i, 0) + 1
        for i in t:
            freqs[i] = freqs.get(i, 0) - 1
        
        for i in freqs.values():
            if not i == 0:
                return False
        return True