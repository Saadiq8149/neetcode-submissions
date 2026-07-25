class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zero = 0
        ones = 0

        for s in students:
            if s == 0: zero += 1
            else: ones += 1

        for s in sandwiches:
            if s == 0 and not zero:
                return ones + zero
            if s == 1 and not ones:
                return ones + zero
            if s == 0:
                zero -= 1   
            if s == 1:
                ones -= 1

        return 0
                