import base64


def str_to_base64(x):
    """文字列をbase64に変換する

    b64encode()はbytes-like objectを引数にとるため
    文字列はencode()でbytes型にして渡す
    """
    return base64.b64encode(x.encode('utf-8'))
