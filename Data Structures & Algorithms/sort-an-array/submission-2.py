import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            pivot = arr[high]
            i = low

            for j in range(low, high):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[high] = arr[high], arr[i]
            return i

        def quicksort(arr, low, high):
            if low < high:
                p = partition(arr, low, high)
                quicksort(arr, low, p - 1)
                quicksort(arr, p + 1, high)     

        quicksort(nums, 0, len(nums)-1)
        return nums