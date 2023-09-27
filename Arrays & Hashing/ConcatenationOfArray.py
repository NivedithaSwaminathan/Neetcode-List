class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        result = [0] * 2* len(nums)
        n = len(nums)

        for i in range(len(nums)):

            result[i] = nums[i]
            result[i + n ] = nums[i]

        return result
