class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''

        for s in strs:
            length = len(s)
            encodedStr += str(length)
            encodedStr += '#'
            encodedStr += s
        return encodedStr
    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            str_list.append(s[i:j])
            i = j
        return str_list