class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mpp = Counter(nums)

        for k,v in mpp.items():
            if v == 1:
                return k