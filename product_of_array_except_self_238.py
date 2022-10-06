def productExceptSelf(nums):
    '''
        1st e left and right array or list banate hbe then oi 2 ta k multiply kore res e nite hbe
        3 ta step & 3 ta for loop
        '''
    # input[1,2,3,4]
    #Product from left to right
    left = [1]*len(nums)   #----> [1,1,1,1]
    for i in range(1,len(nums)):
        left[i] = left[i-1] * nums[i-1]
    
    #product right to left
    right = [1] * len(nums)  # --> [1,1,1,1]
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    
    
    # final output array
    res = [1]*len(nums)
    for i in range(len(nums)):
        res[i] = left[i] * right[i]
    return res
print(productExceptSelf([1,2,3,4]))            
print(productExceptSelf([-1,1,0,-3,3]))            