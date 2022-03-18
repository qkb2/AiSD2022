# SPECS
# I/O requirements: should accept n-seq. of nat. numbers and be able to generate its own random seq.
# types of sequences for the generator:
# random, increasing, decreasing, A-shaped, V-shaped (5 total)


import random


# random seq. generator
def random_generator(n):
    random_list = []
    random.seed()
    for _ in range(0,n):
        random_list.append(random.randint(1, 10*n))

    return random_list


# increasing/decreasing seq. generator
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


# A-shaped/V-shaped seq. generator
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



if __name__ == '__main__':
    a1 = random_generator(10)
    a2 = increasing_generator(50)
    a3 = decreasing_generator(50)
    a4 = a_shaped_generator(50)
    a5 = v_shaped_generator(50)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)