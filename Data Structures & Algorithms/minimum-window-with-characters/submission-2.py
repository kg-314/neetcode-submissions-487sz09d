class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        tCount = {}
        window = {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have = 0
        need = len(tCount)
        
        res = [-1, -1]
        resLen = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and window[c] == tCount[c]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left of our window
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        l = res[0]
        r = res[1]

        return s[l:r+1] if resLen != float("infinity") else ""