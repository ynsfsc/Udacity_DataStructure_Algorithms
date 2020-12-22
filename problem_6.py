def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for element in ints:
        if element > max:
            max = element
        if element < min:
            min = element
    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Input: shuffled list 0~9")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Output: {} Expect: 0, 9".format(get_min_max(l)))
print("-"*50)

print("Input: shuffled list 0~999")
l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(l)) else "Fail")
print("Output: {} Expect: 0, 999".format(get_min_max(l)))
print("-"*50)

l = [0]  # a list containing only

print("Input: [0]")
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")
print("Output: {} Expect: 0, 0".format(get_min_max(l)))
print("-"*50)

l = [0, 1]  # a list containing only

print("Input: [0, 1]")
print ("Pass" if ((0, 1) == get_min_max(l)) else "Fail")
print("Output: {} Expect: 0, 1".format(get_min_max(l)))
print("-"*50)