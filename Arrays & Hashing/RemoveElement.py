# We must remove all occurences of 'val' from nums. All non-val elements must be towards the left of array nums.
# DO NOT SWAP -the question doesn't care about the rest of array nums after the first few non-val elements.
# We use two pointers, k to keep track of the non-val elements and i to traverse the array.
# Starting from index zero, if the ith element matches val, we replace nums[k] with nums[i] and increment both
# If the ith element doesn't match val, we simply increment i and check the next element.
# return k, as it tracks the index of the last non-val element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        k = 0

        while i < len(nums):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                i += 1

            else:
                i += 1

        return k
