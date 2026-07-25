class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(perm=[], pick=[False]*len(nums)):
            if len(perm) == len(nums):
                res.append(perm[:])

            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, pick)
                    perm.pop()
                    pick[i] = False

        backtrack()
        return res

        