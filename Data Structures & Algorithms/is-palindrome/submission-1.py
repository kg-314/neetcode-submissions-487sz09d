class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()
        p1 = 0
        p2 = len(clean) - 1

        while p1 < p2:
            if clean[p1] != clean[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True