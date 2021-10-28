def main():
    f = open('pyvenv.cfg')
    for line in f:
        print(line, end="")
    f.close()


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
