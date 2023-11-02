class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        ptow = {}
        wtop = {}

        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):

            if (pattern[i] in ptow and ptow[pattern[i]] != words[i]) or (words[i] in wtop and wtop[words[i]] != pattern[i]):
                return False

            ptow[pattern[i]] = words[i]
            wtop[words[i]] = pattern[i]

        return True
                
            

        


        
