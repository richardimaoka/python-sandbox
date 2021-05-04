import base64


def base64_to_str(x):
    """base64を文字列に変換する

    b64encode()の戻り値はbytes型であるため
    decode()で文字列にしてから渡す
    """
    return base64.b64decode(x).decode('utf-8')
