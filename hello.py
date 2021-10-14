def main():
    """サンプルプログラムのメイン関数"""
    for i in range(1, 6):
        if i % 2 == 0:
            print("%s is an even number" % i)
        else:
            print("%s is an odd number" % i)

    f = open('pyvenv.cfg')
    for line in f:
        print(line, end="")
    f.close()


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
