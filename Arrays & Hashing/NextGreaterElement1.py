class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [-1] * len(nums1)

        hashmap = {}
        stack = []
        set1 = set(nums1)

        for i,num in enumerate(nums1):
            hashmap[num] = i

        for num in nums2:

            while stack and num>stack[-1]:

                top = stack.pop()
                idx = hashmap[top]
                res[idx] = num

            if num in set1:
                stack.append(num)

        return res

        

       
