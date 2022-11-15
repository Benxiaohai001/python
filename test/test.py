# l = [1,2,3]
# print(l[1:])


class Solution:
    def threeSum(self, nums):
        # re = []
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         if -(nums[i] + nums[j]) in nums[j + 1:]:
        #             mark = 0
        #             for m in re:
        #             # print(nums[i], nums[j])
        #                 if (nums[i] == 0 and nums[j] == 0):
        #                     if [0,0,0] in re:
        #                         mark = 1
        #                     # mark = 1
        #                     break
        #                 elif (nums[i] in m) and (nums[j] in m) and (-((nums[i]) + nums[j]) in m):
        #                     mark = 1
        #                     # re.append([nums[i],nums[j], -(nums[i] + nums[j])])
        #                     break
        #             if mark == 0:
        #                 re.append([nums[i],nums[j], -(nums[i] + nums[j])]) 
        # return re[1:]
        nums.sort()
        # print(nums)
        re = []
        for i in range(len(nums) - 2):
            if (i == 0) or nums[i] != nums[i-1]:
                # l = i + 1
                r = len(nums) - 1
                for j in range(i + 1, len(nums) - 1):
                    if (j == i + 1) or (nums[j] != nums[j-1]):
                        while (nums[i] + nums[j] + nums[r]) > 0:
                            if r <= j: break
                            r -= 1
                        if r <= j: break
                        if (nums[i] + nums[j]) == -nums[r]:
                            re.append((nums[i], nums[j], nums[r]))

                # for j in range(i + 1, len(nums) - 1):
                #     if (j == i + 1) or (nums[j] != nums[j-1]):
                #         for k in range(j+1, len(nums)):
                #             if (k == j + 1) or (nums[k] != nums[k-1]):
                #                 if nums[i] + nums[j] == -nums[k]:
                #                     re.append([nums[i], nums[j], nums[k]])
        return re

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        mark = 0
        if len(nums) > 2:
            for i in range(len(nums)):
                if nums[i] < nums[i - 1]:
                    for j in range(i):
                        if nums[i] < nums[j]:
                            tmp = nums[j]
                            nums[j] = nums[i]
                            nums[i] = tmp
                            mark = 1
                            break
                if mark == 1:
                    break
            if (i != (len(nums) -1 )) or (mark == 1):
                nums_1 = nums[:i]
                nums_1.sort()
                nums_1.reverse()
                for i in range(len(nums_1)):
                    nums[i] = nums_1[i]
                nums.reverse()
        print(nums)
        # print()

    def search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    s = Solution()
    li = [4,5,6,7,0,1,2]
    target = 0
    # print(s.threeSum([0,1,1]))
    # s.nextPermutation(li)
    print(s.search(li, target))
