class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = 1
        curr = 1

        inc = False
        dec = False

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if dec:
                    curr += 1
                else:
                    curr = 2
                    dec = True
                    inc = False

            elif nums[i] < nums[i+1]:
                if inc:
                    curr += 1
                else:
                    curr = 2
                    inc = True
                    dec = False

            else:
                curr = 1
                inc = dec = False

            maxLen = max(maxLen, curr)
        return maxLen