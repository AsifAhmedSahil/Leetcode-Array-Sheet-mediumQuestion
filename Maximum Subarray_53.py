def maxSubArray(nums):
    max_sum = nums[0]
    current_Sum = 0
    
    for num in nums:
        if current_Sum < 0:
            current_Sum = 0
        
        current_Sum = current_Sum + num
        max_sum = max(current_Sum , max_sum)
        
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))