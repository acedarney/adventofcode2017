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
    for row in data.iterrows():
        # combos = list(permutations(row[1]))
        # print(combos)
        pass
    for pair in permutations(data.ix[0]):
        print(pair)

    # return results



if __name__ == '__main__':
    # result = main()
    result = main2()
    # print(result)
