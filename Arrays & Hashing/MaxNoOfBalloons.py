class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        ctr = collections.Counter("balloon")

        res = [0] * len(ctr.keys())

        ctr2 = collections.Counter(text)
        i = 0
        for k in ctr.keys():

            if k in ctr2:
                res[i] = ctr2[k]//ctr[k]
                i += 1




        return min(res)

