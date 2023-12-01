class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1


        k = k % len(nums)

        reverse(0, len(nums) - 1)     # reverses the entire array
        reverse(0, k - 1)      # reverses the first k elements or till (k - 1) index
        reverse(k, len(nums) - 1)      # reverses the rest of the elements


         
        