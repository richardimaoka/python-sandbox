import sys


def main():
    p = Point(4, 5)
    print("{0.x}, {0.y}".format(p))
    print("{0}, {1}".format(p.x, p.y))

    data = {'x': 4, 'y': 5}
    print("{0[x]}, {0[y]}".format(data))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    main()
