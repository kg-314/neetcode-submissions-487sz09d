class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Have another map of freqs as key, list of anagrams as value.
        anagramFreqMap = defaultdict(list)

        for i in strs:
            freqs = [0] * 26
            for j in i:
                freqs[ord(j) - ord('a')] += 1
            anagramFreqMap[tuple(freqs)].append(i)
        
        result = []
        for v in anagramFreqMap.values():
            result.append(v)
        return result