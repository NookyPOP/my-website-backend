import uuid


def generate_random_string():
    """
    生成一个随机的 UUID 字符串。

    Returns:
      生成的随机 UUID 字符串。
    """
    random_string = str(uuid.uuid4())
    return random_string
