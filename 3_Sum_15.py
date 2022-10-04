def threeSum(nums):
    res = []
    nums.sort()
    print(nums)

    length = len(nums)

       # loop krte jai lenght -2 porjonto cholbe loop bcoz 2 ta space e pointer lagailam
    for i in range(length-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = length-1

        while l<r:
            total = nums[i] + nums[l] + nums[r]

            if total<0:
                    # we know our list is sorted so its also left side
                    l = l+1
            elif total>0:
                    r = r-1
            else:
                res.append([nums[i], nums[l], nums[r]])

                while l<r and nums[l] == nums[l+1]:
                        l = l+1
                while l<r and nums[r] == nums[r-1]:
                        r = r-1

                l = l+1
                r = r-1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
