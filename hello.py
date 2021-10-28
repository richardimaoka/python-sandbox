def main():
    with open('pyvenv.cfg') as f:
        for line in f:
            print(line, end="")


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
