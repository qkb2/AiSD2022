import generator


if __name__ == '__main__':
    a1 = generator.random_generator(10)
    a2 = generator.increasing_generator(50)
    a3 = generator.decreasing_generator(50)
    a4 = generator.a_shaped_generator(50)
    a5 = generator.v_shaped_generator(50)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)