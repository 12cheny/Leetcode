#--codeing:UTF-8--
#Two Sum
class Solution(object):
  def twoSum(self,nums,target):
    """
        :type nums: List[int]
        :type target: int
        :rty
    """
    answer=[]
    for i in range(len(nums)):
      for j in range(len(nums)-i-1):
        if nums[i]+nums[j+i+1]==target:
          answer.append(i)
          answer.append(j+i+1)
          return answer
