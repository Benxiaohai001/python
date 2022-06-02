class Solution:
    def largestRectangleArea(self, heights):
        s = 0
        for i in range(len(heights)):
            con = 1
            m = 1
            if (i - m) >= 0:
                while heights[i - m] >= heights[i]:
                    con += 1
                    m += 1
                    if m > i:
                        break
            n = 1
            if (i + n) <= (len(heights) - 1):
                while heights[i + n] >= heights[i]:
                    con += 1
                    n += 1
                    if (n+i) > (len(heights) - 1):
                        break
            if s < (heights[i] * con):
                s = heights[i] * con
        return s


if __name__ == '__main__':
    s = Solution()
    # l = list()
    li = [2, 1, 5, 6, 2, 3]
    s.largestRectangleArea(li)