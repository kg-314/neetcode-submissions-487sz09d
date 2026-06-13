class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0
        maxFreq = 0

        l = 0
        r = 0

        # replacements needed = window size - most frequent character
        # cleaner version

        for r in range(len(s)):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxFreq = max(maxFreq, freqs[s[r]])

            while r - l + 1 - maxFreq > k:
                freqs[s[l]] = freqs.get(s[l]) - 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res