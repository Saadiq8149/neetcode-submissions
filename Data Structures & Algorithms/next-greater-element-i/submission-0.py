class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pivot = None

        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    pivot = j
                    break
            for n in nums2[pivot:]:
                if n > nums2[pivot]:
                    res.append(n)
                    break
            else:
                res.append(-1)

        return res
                    