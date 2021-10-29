import sys


def main():
    print("{0:04} {1:02}".format(2, 8))


def echo(in_, out):
    for line in in_:
        out.write("{0} {1}".format(len(line), line))


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
