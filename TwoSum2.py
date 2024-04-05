# Beats 78.2% in memory and 50.11% in time

class Solution(object):
  def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      for x in range(len(nums)):
          try:
              z = nums.index(target - nums[x])
              if z != x:
                  return [x,z]
          except ValueError:
              continue