import sys


def main():
    print("{0:04} {1:02}".format(2, 8))
    print("{0:05} {1:02}".format(2, 8))
    print("{0:06} {1:02}".format(2, 8))
    print("{0:6} {1:02}".format(232, 8))
    print("{0:6} {1:02}".format(232.3, 8))
    print("{0:06} {1:02}".format(232.3, 8))
    # invalid
    # print("{0:0x6} {1:02}".format(232.3, 8))
    # invalid
    # print("{0:x6} {1:02}".format(232.3, 8))
    print("{0:04} {1:02}".format(2, 8))
    print("{0:04} {0:02}".format(2, 8))
    # invlid
    # print("{0:04} {3:02}".format(2, 8))
    print("{0:,}".format(9999999999999999))


def echo(in_, out):
    for line in in_:
        out.write("{0} {1}".format(len(line), line))


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
