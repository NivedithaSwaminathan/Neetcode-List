class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap =[0] * 26

        for ch in s:

            hashmap[ord(ch) - ord('a')] += 1

        for ch in t:
            hashmap[ord(ch) - ord('a')] -= 1

        for num in hashmap:

            if num:
                return False

        return True
