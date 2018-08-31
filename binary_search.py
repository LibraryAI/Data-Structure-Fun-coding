def binary_search(lst, cond):
    ''' 
	Binary Search 활용하여 lst 내에서 cond 조건을 만족하는 최소의 원소를 반환
	lst 는 오름차순으로 정렬되어있다고 가정
    
    ex) binary_search([1,2,3,4,5], lambda x: x>1) returns 2
    '''
    end = len(lst) - 1
    start = 0
    mid = (end + start)//2
    condition = cond

    if start > end:
    	return False

    if start == end:
    	if condition(lst[mid]) is True:
    		return lst[mid]
    	else:
    		return False
    else:
    	if condition(lst[mid]) is True:
    		if binary_search(lst[:mid], cond) is False:
    			return lst[mid]
    		else:
    			return binary_search(lst[:mid], cond)
    	else:
    		return binary_search(lst[mid+1:], cond)
