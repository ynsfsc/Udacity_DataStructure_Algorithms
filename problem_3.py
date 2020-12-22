def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    def merge(list1, list2):
        length1 = len(list1)
        length2 = len(list2)
        length = length1 + length2
        output = []
        index1 = 0
        index2 = 0
        for i in range(length):
            if list1[index1] < list2[index2]:
                output.append(list2[index2])
                index2 += 1
            else:
                output.append(list1[index1])
                index1 += 1
            
            if index1 == length1:
                output = output + list2[index2:]
                break
            if index2 == length2:
                output = output + list1[index1:]
                break
        return output
    
    def merge_sort(input_list):
        # sort a list into decending form
        if len(input_list) <= 1:
            return input_list
        
        mid = len(input_list) // 2
        
        # 
        left_list = merge_sort(input_list[0:mid])
        right_list = merge_sort(input_list[mid:])
        
        return merge(left_list, right_list)
    
    first_num = 0
    second_num = 0
    switch = 0
    for digit in merge_sort(input_list):
        if switch == 0:
            first_num = first_num*10 + digit
            switch = 1
        else:
            second_num = second_num*10 + digit
            switch = 0
    return [first_num, second_num]

def test_function(test_case):
    print("-"*40)
    print("Input:")
    print(test_case[0])
    print("Output:")
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    print("Expect:")
    print(solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[1,0], [1,0]]
test_function(test_case)