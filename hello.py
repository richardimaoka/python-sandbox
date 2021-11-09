import sys
import fileinput
import argparse
import operator


def sum_products(filename):
    with open(filename) as f:
        results = {}
        for line in f:
            parts = line.split(",")
            title = parts[0]
            count = int(parts[1])
            last_count = results.get(title, 0)
            results[title] = last_count + count
    return results


def print_results(results):
    for key, value in sorted(results.items(), key=operator.itemgetter(1)):
        print(key, value)


def main():
    print_results(sum_products('products.txt'))


if __name__ == '__main__':
    main()
