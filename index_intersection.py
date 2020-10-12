# Input: List of List of index ( here index is index of user input list containing sentences )
# Output: Output will contain intersection of comman elemnt which is inside list.

def index_intersection(index_list):
	if type(index_list) != list:
		print("Invalid input at point #33")
		return
	like_map = [0]*100001
	for l in range(0,len(index_list)-1):
		for element in index_list[l]:
			like_map[element]+=1
	ans = []
	for element in index_list[len(index_list)-1]:
		like_map[element]+=1;
		if like_map[element] == len(index_list):
			ans.append(element)
	return ans
