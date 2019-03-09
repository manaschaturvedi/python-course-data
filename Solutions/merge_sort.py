def merge_sorted_lists(li1,li2):
	ans = []
	len1 = len(li1)
	len2 = len(li2)
	i = j = 0

	while i<len1 or j<len2:

		if i<len1 and j<len2:
			if(li1[i]<=li2[j]):
				ans.append(li1[i])
				i += 1
			else:
				ans.append(li2[j])
				j += 1

		elif i<len1:
			ans.append(li1[i])
			i += 1

		elif j<len2:
			ans.append(li2[j])
			j += 1
	return ans

# print merge_sorted_lists([1,3,4,53],[2,5,33,56])

def merge_sort(li):
	if len(li) <= 1:
		return li
	else:
		mid = int(len(li)/2)
		left = li[:mid]
		right = li[mid:]
		sorted_left = merge_sort(left)
		sorted_right = merge_sort(right)
		return merge_sorted_lists(sorted_left,sorted_right)

print(merge_sort([38,27,43,3,9,82,42,10,-1]))