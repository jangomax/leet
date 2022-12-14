class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = [nums[0]]

        for num in nums[1:]:
            sum.append(sum[-1] + num)

        return sum
