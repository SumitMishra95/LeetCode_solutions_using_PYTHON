class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                if nums.index(diff) == i:
                    continue
                return [i,nums.index(diff)]
