def contain_duplicates(nums):

	# nums = [1, 2, 3, 1] 
	length = len(nums) 
	for i in range(length):
		# j = i + 1 
		for j in range(i+1, length) :
			if nums[i] == nums[j]:
				print("true")
				return 0
	print("false")
	return 0	

# contain_duplicates([1, 2])	
def contains_duplicates1(nums):
	length = len(nums)
	set1 = set(nums) 
	if len(nums) == len(set1):
		print("false") 
		return 0 
	else:
		print("true")
		return 0	

contains_duplicates1([1, 2])	