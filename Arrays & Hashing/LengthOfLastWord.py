# TO FIND THE LENGTH OF THE LAST WORD IN THE STRING
# We traverse the string from the last character.
# We identify if it is the first whitepace by checking wordlen is still 0, and keep decrementing i until we find a character.
# We decrement the pointer until a word is found, then we find the length of that word until the next whitespace or end of string is reached.

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
