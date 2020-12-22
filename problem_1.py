def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1 or number == 0:
        return number
    
    left = 0
    right = number
    root = (right - left) // 2 + left
    while left != root:
        if root * root > number:
            right = root
        elif root * root < number:
            left = root
        else:
            break
        
        root = (right - left) // 2 + left

    return root

def test_function(test_case):
    num = test_case[0]
    expect = test_case[1]
    print("-"*40)
    print("Input:")
    print(num)
    print("Output:")
    print(sqrt(num))
    print("Expect:")
    print(expect)
    if sqrt(num) == expect:
        print("Pass")
    else:
        print("Fail")

test_cases = [[9,3],[0,0],[16,4],[1,1],[27,5]]

for test_case in test_cases:
    test_function(test_case)