class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # last index 
        last = m + n - 1

        #merge in reverse order
        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[last] = nums2[n-1]
                n = n - 1
            elif nums1[m-1] >= nums2[n-1]:
                nums1[last] = nums1[m-1]
                m = m - 1
            last = last - 1
        
        #fill leftover nums2 in nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


        