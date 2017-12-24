def main():
    count, total = 0, 0
    with open('aoc_2017-4_data.txt') as f:
        for line in f:
            total += 1
            words = line.split()
            for i, word in enumerate(words):
                if word in words[i + 1:]:
                    count += 1
                    break
    return total - count


if __name__ == '__main__':
    result = main()
    print(result)
