# We use a hashset to keep track of duplicates, if any. 
# The lookup time for a hashset is O(1), as opposed to a hashmap which is O(n). 
# Traverse the array and add to the hashset if it doesn't already exist. If it does, a duplicate has been found.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
