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
        length = ''
        int_length = 0
        cnt = 0
        while i < len(s):
            if s[i] == '#':
                i += 1
                int_length = int(length)
                length = ''
                str_list.append('')
                for j in range(i, i + int_length):
                    str_list[cnt] += s[j]
                cnt += 1
                i += int_length
            if i < len(s):
                length += s[i]
            i += 1
        return str_list