def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def pivot(input_list, left, right):
        # get the pivot index(the smallest element index)
        if right - left == 0:
            return left
        if right - left == 1:
            return left if input_list[left] < input_list[right] else right
        
        mid = (right - left) // 2 + left
        if input_list[mid] > input_list[right]:
            return pivot(input_list, mid + 1, right)
        if input_list[mid] < input_list[right]:
            return pivot(input_list, left, mid)
    
    def search(input_list, number, left, right):
        # search number in a sorted array
        if left > right:
            return -1
        
        mid = (right - left) // 2 + left
        if input_list[mid] == number:
            return mid
        if input_list[mid] < number:
            return search(input_list, number, mid + 1, right)
        
        return search(input_list, number, left, mid - 1)
    
    length = len(input_list)
    pivot = pivot(input_list, 0, length - 1)
    # if no pivot
    if pivot == 0:
        output = search(input_list, number, 0, length - 1)
    # if pivot
    else:
        if input_list[0] > number:
            output = search(input_list, number, pivot, length - 1)
        else:
            output = search(input_list, number, 0, pivot)
    return output

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    print("-"*40)
    input_list = test_case[0]
    number = test_case[1]
    print("Input:")
    print(input_list, number)
    print("Output:")
    print(rotated_array_search(input_list, number))
    print("Expect:")
    print(linear_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2])