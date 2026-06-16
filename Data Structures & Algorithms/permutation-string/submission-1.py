class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # This code is O(n*m) where n is len(s2) and m is len(s1)
        # b/c once I reach the right window size I have to loop through s1
        # to check every possible window in s2.
        if len(s2) < len(s1):
            return False
        freq = {}

        for c in s1:
            freq[c] = 1 + freq.get(c, 0)

        p1 = 0
        
        for p2 in range(len(s2)):
            freq[s2[p2]] = -1 + freq.get(s2[p2], 0)
            
            if p2 - p1 + 1 == len(s1):
                perm = True
                for i in s1:
                    if freq[i] != 0:
                        perm = False
                if perm == True:
                    return True
                freq[s2[p1]] = 1 + freq.get(s2[p1])
                p1 += 1
        return False
