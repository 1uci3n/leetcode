class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = list(range(1, len(nums)+1))
        for i in range(len(nums)):
            a[nums[i] - 1] = 0
        point = 0
        for _ in range(len(a)):
            if a[point] == 0:
                del a[point]
                continue
            point += 1
        return a
