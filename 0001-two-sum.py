
def twoSum(nums, target):
    d = {}
    for index, num in enumerate(nums):
        rem = target - num
        if rem in d:
            return [d[rem], index]
        d[num] = index

nums = [4,3,2,1]
target =  6
print(twoSum(nums, target))