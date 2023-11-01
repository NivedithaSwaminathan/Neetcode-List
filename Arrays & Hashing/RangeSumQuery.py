class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums

        # we pre-compute the prefix sums to save time
        self.psum = [0] * (len(nums) + 1)

        for i in range(len(self.nums)):

            self.psum[i+1] = self.psum[i] + self.nums[i]

        

    def sumRange(self, left: int, right: int) -> int:

        res = self.psum[right+1] - self.psum[left]
        return res

        

        
