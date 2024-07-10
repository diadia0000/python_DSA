from time import *
from random import randint
def Intersection_set(a, b):
    """
        average time O(min(len(a),len(b)))
        worst case O(len(a) * len(b))
    """

    return list(set(a) & set(b))


def Intersection_for(a, b):
    """
        time O(n^2)
    """
    s = time()
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(b[i])
    e = time()
    return result,e-s


def Intersection_counter(a, b):
    """
        time O(a+b)
    """
    ans = []
    arr = a + b
    counter = {}
    s = time()
    for i in arr:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
        if counter[i] == 2:
            ans.append(i)
    e = time()
    return ans,e-s

# case
a = [randint(1,500000) for i in range(50000)]
b = [randint(1,500000) for j in range(50000)]
s = time()
intersection_set = Intersection_set(a, b)
e = time()
set_time = e-s

intersection_for, for_time = Intersection_for(a, b)
intersection_counter, counter_time = Intersection_counter(a, b)
print(f"set_time = {set_time}")
print(f"for_time = {for_time}")
print(f"counter_time = {counter_time}")
