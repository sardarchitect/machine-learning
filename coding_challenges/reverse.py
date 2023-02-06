nums = [1,2,3,4,5, 1, 3]
print(nums)

unique_nums = []
[unique_nums.append(i) for i in nums if i not in unique_nums]

if nums == unique_nums:
    print("There are no duplicates")
else: 
    print("there are duplicates")