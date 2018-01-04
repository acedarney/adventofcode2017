import pandas as pd

def next_step(idx, arr, counter):
    new_idx = idx + arr[idx]
    arr[idx] += 1
    counter += 1
    return new_idx, arr, counter


def next_step2(idx, arr, counter):
    new_idx = idx + arr[idx]
    if arr[idx] > 2:
        arr[idx] += -1
    else:
        arr[idx] += 1
    counter += 1
    return new_idx, arr, counter


def main(arr):
    idx = arr[0]
    counter = 0
    while True:
        if idx < len(arr):
            idx, arr, counter = next_step(idx, arr, counter)
            print(idx, counter)
        else:
            break


def main2(arr):
    idx = arr[0]
    counter = 0
    while True:
        if idx < len(arr):
            idx, arr, counter = next_step2(idx, arr, counter)
            # print(idx, counter)
        else:
            print(counter)
            break


def create_array(filename):
    df = pd.read_csv(filename, header=None)
    arr = list(df[0])
    return arr

if __name__ == '__main__':
    # arr = [0, 3, 0, 1, -3]
    arr = create_array('aoc_2017-5_data.txt')
    main2(arr)
