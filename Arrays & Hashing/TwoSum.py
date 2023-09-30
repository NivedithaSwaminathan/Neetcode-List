# To find 2 unique nums that add up to a target
# We use a hashmap to keep track of (target-nums[i]) using the difference as the key, and the ith index as the value.
# For each number, if the difference already exists in the hashmap, then we have found the other number that makes up the target.
# If we reach the end of the array without finding any difference in the hashmap, there exists no such pair.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):

            diff = target - num

            if diff in hashmap:

                return [hashmap[diff], i]

            hashmap[num] = i

        return -1
