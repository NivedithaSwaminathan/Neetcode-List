# Check if s is a subsequence of t
# First check is to see if s isn't longer than t.
# We work with two pointers, one to traverse s and the other to traverse t. 
# We try to find characters of s in t and update a flag along the way.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        i, j = 0, 0
        flag = 0

        while j < len(t):

            if flag == len(s):
                return True

            if s[i] == t[j]:
                flag += 1
                i += 1
                
            j += 1

        if flag == len(s):
            return True

        return False
