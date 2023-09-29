class Solution:
    def lengthOfLastWord(self, s: str) -> int:

       wordlen = 0

       i = len(s) - 1

       while i >=0:

           if s[i] == " " and wordlen ==0:
               i -= 1

           else:

               if s[i] == " ":
                   return wordlen

               else:
                    wordlen += 1
                    i -= 1

       return wordlen
