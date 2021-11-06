import sys
import fileinput
import argparse


def main():
    with open('products.txt') as f:
        for line in f:
            parts = line.split(',')
            title = parts[0]
            count = int(parts[1])
            results = {}
            last_count = results.get(title, 0)
            results[title] = last_count + count
            print(results)


if __name__ == '__main__':
    main()
