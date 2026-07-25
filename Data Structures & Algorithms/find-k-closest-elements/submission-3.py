class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = arr[0]
        closestIndex = 0

        for i, n in enumerate(arr):
            if abs(closest-x) > abs(n-x):
                closest = n
                closestIndex = i

        res = [closest]
        
        l = closestIndex - 1
        r = closestIndex + 1

        while len(res) < k and r < len(arr) and l >= 0:
            if abs(arr[r] - x) > abs(arr[l] - x):
                res.append(arr[l])
                l -= 1
            elif abs(arr[r] - x) < abs(arr[l] - x):
                res.append(arr[r])
                r += 1
            else:
                if arr[l] < arr[r]:
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1

        if len(res) < k:
            if l >= 0:
                while len(res) < k and l >= 0:
                    res.append(arr[l])
                    l -= 1
            elif r < len(arr):
                while len(res) < k and r < len(arr):
                    res.append(arr[r])
                    r += 1

        res.sort()
        return res