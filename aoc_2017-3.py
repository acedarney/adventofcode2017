import math


def main(inp):
    vert = [1]
    count = 1

    diff = [1, 3] * 20
    increment = [3, 4]

    while count < 2000:
        increment.append(increment[-1] + diff[1])
        increment.append(increment[-1] + diff[0])
        count += 1

    for value in increment:
        vert.append(vert[-1] + value)

    # print(vert)

    horiz_dist = [abs(inp - val) for val in vert]
    min_idx = horiz_dist.index(min(horiz_dist))
    # print(min_idx)
    # print(horiz_dist)
    vert_dist = math.ceil(vert.index(vert[min_idx]) / 2)

    return min(horiz_dist) + vert_dist


if __name__ == '__main__':
    # a = main(31)
    # b = main(77)
    # c = main(7)
    # print(a, b, c)
    print('Result: ', main(312051))
