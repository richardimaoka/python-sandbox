import sys
import fileinput
import argparse


def main():
    with open('products.txt') as f:
        for line in f:
            sys.stdout.write(line)


if __name__ == '__main__':
    main()
