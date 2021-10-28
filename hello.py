import sys


def main():
    echo(sys.stdin, sys.stdout)


def echo(in_, out):
    for line in in_:
        out.write(line)


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
