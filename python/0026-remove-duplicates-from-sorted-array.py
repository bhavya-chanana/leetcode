# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(nums):
    count = 0
    for i in range(len(nums)):
        if i<len(nums)-1 and nums[i] == nums[i+1]:
            continue
        nums[count] = nums[i]   #as the array is sorted and count = distinct values in array thus we can replace the no at count index in num array with the next distinct no
        # print(nums)
        count+=1
    return count

nums = [1,1,2,2,3,4,4,5]
print(removeDuplicates(nums))