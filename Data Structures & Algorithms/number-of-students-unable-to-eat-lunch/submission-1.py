class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mpp = {0: 0, 1: 0}

        for s in students:
            mpp[s] += 1


        for s in sandwiches:
            if mpp[s] > 0:
                mpp[s] -= 1
            else:
                return mpp[0] + mpp[1]

        return 0