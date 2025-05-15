def two_sum(nums, target):
   
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return None


input_list = input("Enter a list of numbers separated by spaces: ")
nums = list(map(int, input_list.split()))

target = int(input("Enter the target sum: "))


result = two_sum(nums, target)

if result:
    print(f"Indices of numbers that add up to {target}: {result}")
else:
    print("No two numbers found that add up to the target.")
