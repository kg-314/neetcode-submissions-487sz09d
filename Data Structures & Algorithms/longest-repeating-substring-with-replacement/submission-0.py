class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0
        largestFreq = 0

        l = 0
        r = 0

        # replacements needed = window size - most frequent character

        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1

            if freqs[s[r]] > largestFreq:
                largestFreq = freqs[s[r]]
                res = max(res, (r - l + 1))
            elif ((r - l + 1) - largestFreq) <= k:
                res = max(res, (r - l + 1))

            while ((r - l + 1) - largestFreq) > k:
                freqs[s[l]] = freqs.get(s[l]) - 1
                l += 1
            r += 1
        return res