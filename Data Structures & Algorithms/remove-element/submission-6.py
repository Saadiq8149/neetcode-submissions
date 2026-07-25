class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = Counter(nums)

        index = 0
        for k, v in count.items():
            if k != val:
                for _ in range(v):
                    nums[index] = k
                    index += 1

        return len(nums) - count[val]