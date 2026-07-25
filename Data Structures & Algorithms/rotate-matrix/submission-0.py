class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(m):
            for i in range(len(m)):
                for j in range(i):
                    temp = m[i][j]
                    m[i][j] = m[j][i]
                    m[j][i] = temp

        def reverse_rows(m):
            for i in range(len(m)):
                m[i] = reversed(m[i])

        transpose(matrix)
        reverse_rows(matrix)