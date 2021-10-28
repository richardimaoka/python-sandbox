def main():
    with open('pyvenv.cfg') as f:
        for line in f:
            print(line, end="")
        f.close()
        f.close()
        print('f.close() is called twice')


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
