class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_num = max(max_num, current_sum)
        return max_num
#TODO: divide and concour solution

if __name__ == '__main__':
    result = Solution().maxSubArray([1, 2, 3, -1])
    print result