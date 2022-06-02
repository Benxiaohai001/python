class Solution:
    def reconstructQueue(self, people):
        q = []
        for i in range(len(people)):
            con = 0
            if q != []:
                for j in q:
                    if j[0] >= people[i][0]:
                        con += 1
            q.append([people[i][0], con])
        return q


if __name__ == "__main__":
    p = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    s = Solution()
    s.reconstructQueue(p)