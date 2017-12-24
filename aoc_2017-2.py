import pandas as pd
from itertools import permutations


def main():
    data = pd.read_table('aoc_2017-2_data.txt', header=None)
    # print(data.head())
    data['max'] = data.max(axis=1)
    data['min'] = data.min(axis=1)
    data['diff'] = data['max'] - data['min']
    print(data[['max', 'min', 'diff']])
    return data['diff'].sum()


def main2():
    data = pd.read_table('aoc_2017-2_data.txt', header=None)
    results = []
    for row in data.iterrows():
        for pair in permutations(row[1], 2):
            if pair[0] % pair[1] == 0:
                # print(pair[0], pair[1], pair[0]/pair[1])
                results.append(pair[0] / pair[1])
            else:
                pass
    return sum(results)


if __name__ == '__main__':
    # result = main()
    result = main2()
    print(result)
