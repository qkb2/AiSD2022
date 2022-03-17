#SPECS
#I/O requirements: should accept n-seq. of nat. numbers and be able to generate its own random seq.
#types of sequences for the generator:
#random, increasing, decreasing, A-shaped, V-shaped (5 total)


import random


#DONE: random seq. generator
def random_generator(n):
    random_list = []
    random.seed()
    for _ in range(0,n):
        random_list.append(random.randint(1, 10*n))

    return random_list


#DONE: increasing/decreasing seq. generator
def increasing_generator(n):
    random.seed()
    random_list = [random.randint(1,10*n)]
    for i in range(0,n-1):
        random_list.append(random_list[i]+random.randint(0,n//10))

    return random_list


def decreasing_generator(n):
    random.seed()
    random_list = [random.randint(9*n,10*n)]
    for i in range(0,n-1):
        random_list.append(random_list[i]-random.randint(0,n//10))

    return random_list


#DONE: A-shaped/V-shaped seq. generator
def a_shaped_generator(n):
    array = increasing_generator((n + 1) // 2)
    half_array = decreasing_generator(n // 2)
    array.extend(half_array)
    return array


def v_shaped_generator(n):
    array = decreasing_generator((n + 1) // 2)
    half_array = increasing_generator(n // 2)
    array.extend(half_array)
    return array


