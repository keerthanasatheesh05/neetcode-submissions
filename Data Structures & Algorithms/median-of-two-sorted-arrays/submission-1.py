class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        numo = nums1 + nums2
        num = sorted(numo)
        n = len (num)
        
        if n % 2 == 1:
            median = num[n//2]
            
        else:
            median = (num[n//2-1] + num[n//2] ) / 2
        
        return median

    
       

        