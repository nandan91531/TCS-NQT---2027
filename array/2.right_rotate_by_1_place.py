def right_rotate(nums):
    n = len(nums)
    temp = nums[n-1]
    j=1
    for i in range(n-1,0,-1):
        nums[n-j] = nums[n-j-1]
        j+=1
    nums[0] = temp
    return nums
        
        
# Example 1:
# nums = [1, 2, 3, 4, 5]
# Right rotate = [5, 1, 2, 3, 4]

# Example 2:
# nums = [10, 20, 30, 40]
# Right rotate = [40, 10, 20, 30]

# Example 3:
# nums = [1, 2, 3]
# Right rotate = [3, 1, 2]