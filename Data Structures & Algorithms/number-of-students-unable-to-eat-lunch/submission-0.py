class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = [0, 0]
        for s in students:
            cnt[s] += 1

        for s in sandwiches:
            if cnt[s] == 0:
                break
            cnt[s] -= 1

        return cnt[0] + cnt[1]
        


        