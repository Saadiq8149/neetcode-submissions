class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(i=0, curr=[]):
            if i >= len(nums):
                res.append(curr[:])
                return 

            curr.append(nums[i])
            recurse(i+1, curr)
            curr.pop()
            recurse(i+1, curr)

        recurse()
        return res
