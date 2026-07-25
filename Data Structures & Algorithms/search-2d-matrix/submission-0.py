class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        top = 0
        bottom = len(matrix) - 1
        row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            low = matrix[mid][0]
            high = matrix[mid][-1]

            if low <= target <= high:
                row = mid
                break
            elif target < low:
                bottom = mid - 1
            else:
                top = mid + 1

        if row == -1:
            return False

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            number = matrix[row][mid]

            if number == target:
                return True
            elif target < number:
                right = mid - 1
            else:
                left = mid + 1

        return False
