class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # hashset has O(1) lookup time
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
