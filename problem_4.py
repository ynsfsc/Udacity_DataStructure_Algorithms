def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # traverse once and save the frequency of 0,1,2
    count_dict = {0:0, 1:0, 2:0}
    for element in input_list:
        count_dict[element] += 1
        
    # return the output list according to the frequency
    return [0]*count_dict[0] + [1]*count_dict[1] + [2]*count_dict[2]

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print("Input:")
    print(test_case)
    print("-"*40)
    print("Output:")
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
        print("-"*40)
    else:
        print("Fail")
        print("-"*40)

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2])