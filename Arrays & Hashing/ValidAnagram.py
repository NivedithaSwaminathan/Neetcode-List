# A string s is an anagram of string t is all the letters of s are in t.
# Our first check is to verify the string lengths.
# We create one hashmap whose indices are used to keep track of letters and we update the count of s.
# We traverse through t and decrement the count of the letters.
# For s to be an anagram of t, the hashmap should be all zeros. If not, we return false.

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
