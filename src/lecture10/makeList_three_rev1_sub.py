nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    print(num + ":" + nums)
    if (num % 3) != 0:
        nums.remove(num)
print(nums)
