# Create an empty string to build the longest common prefix.
# We pick the first word as the reference string, and traverse the entire length of that string. (we can also pick the min string)
# For each word in the list, we check if the ith character matches the ith character of our reference string.
# If i has reached the length of the current word, or if there is a mismatch in the ith character, we return the prefix.
# Otherwise we add the current matchign ith character to our empty prefix string.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return prefix

            prefix += word[i]
            
                
        return prefix
