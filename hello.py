def main():
    s = 'あ'
    b = s.encode('utf-8')
    print(s)
    print(b)
    c = b'\xe3\x81\x82'
    d = c.decode('utf-8')
    e = str(c)
    print(d)
    print(e)


def docstring_test():
    """this is for documentation"""
    return True


if __name__ == "__main__":
    main()
