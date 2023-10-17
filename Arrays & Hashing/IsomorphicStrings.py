# Check if two strings t and s are isomorphic (characters in s can be replaced to get t)
# If the strings are of unqeual length, we can directly retur False
# Traverse the length of the array and check every ith character and it's corresponding value in the mapping dict, if it exists.
# If there is a mismatch, we needn't check further and we can return False.
# Else, create a Counter to map every th character in s to its corresponding character in t and vice versa.
# If we reach the end of the array, we return True.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            if (s[i] in s_to_t and s_to_t[s[i]] != t[i]) or ( t[i] in t_to_s and t_to_s[t[i]] != s[i]):
                return False

            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

        return True

        
        
