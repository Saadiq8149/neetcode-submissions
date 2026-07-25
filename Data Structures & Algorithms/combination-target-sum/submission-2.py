class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(i=0, curr=[]):
            s = sum(curr)
            if i >= len(nums) or s >= target:
                if s == target:
                    res.append(curr[:])
                return

            curr.append(nums[i])
            recurse(i, curr)
            curr.pop()
            recurse(i+1, curr)

        recurse()
        return res
