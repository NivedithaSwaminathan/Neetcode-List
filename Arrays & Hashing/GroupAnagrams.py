# We create a dictionary where the value would be the list of words that form a specific anagram
# We create a Counter of each word by assuming char 'a' to be index 0 and so on.
# Once we get that array of character of counts, we convert that to a tuple and use it as the key to our dictionary.
# Words which have the same character count are grouped together (these words are anagrams).
# We return the values of the dictionary.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for ch in word:

                key[ord(ch) - ord('a')] += 1

            res[tuple(key)].append(word)

        return res.values()
