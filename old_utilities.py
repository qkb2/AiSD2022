import random


def decreasing_generator(n, k):
    random.seed()
    random_list = [random.randint(9 * k // 10, k)]
    for i in range(0, n - 1):
        random_list.append(random_list[i] - random.randint(0, k // n))

    return random_list


if __name__ == "__main__":
    nn = int(input("n: "))
    kk = int(input("k: "))
    print(decreasing_generator(nn, kk))  # using k = 10*n provides reasonable results
