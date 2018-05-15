#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums1=nums1+nums2
        nums1.sort()
        if len(nums1)%2==0:
            return (float(nums1[len(nums1)/2])+float(nums1[len(nums1)/2-1]))/2
        else:
            return nums1[(len(nums1)-1)/2]
           
           
利用statistics模块　
return statistics.median(nums1+nums2)
