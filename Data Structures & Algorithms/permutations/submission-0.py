class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums):
            if i == len(nums):
                return [[]]

            resPerms = []
            perms = helper(i+1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pC = p.copy()
                    pC.insert(j, nums[i])
                    resPerms.append(pC)

            return resPerms

        return helper(0, nums)