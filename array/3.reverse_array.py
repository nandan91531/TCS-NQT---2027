def reverse(nums):
    n = len(nums)
    start = 0
    end = n-1
    while start<=end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end -= 1
    return nums

# [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]
# [10, 20, 30, 40] => [40, 30, 20, 10]
# [1, 2, 3] => [3, 2, 1]