nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = nums[:]
for num in nums2:
    print(num)
    if (num % 3) != 0:
        nums.remove(num)
print(nums)
