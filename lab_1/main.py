
def get_reshuffle(key: str) -> list[int]:
    """
    Returns a sequense of columns for ensoding by key
    :param key: key for encoding
    :return: sequense of columns
    """
    key = "".join(c for c in key if c not in r'!./,?"\| ')
    key_dict = {}
    for i, letter in enumerate(key):
        key_dict[i] = letter
    sort_list = list(key_dict.keys())
    sort_list = sorted(sort_list, key=lambda k: key_dict[k])
    return sort_list


def prepare_text(src_text: str, key_len: int) -> str:
    text = src_text
    while (len(text) % (4 * key_len)) != 0:
        text += " "
        text += src_text[:((key_len * 4) - (len(text) % (4 * key_len)))]
    return text


def make_reshuffle(src_text: str, key: str) -> str:
    """
    Returns encoded text
    :param text: src text
    :param key: key for encoding
    :return: encoded text
    """
    sort_list = get_reshuffle(key)
    res = ""
    text = prepare_text(src_text, len(sort_list))
    while len(text) > 0:
        table_text = []
        table_w = len(sort_list)
        for i in range(0, table_w):
            if i % 2 == 0:
                table_text.append(text[:4])
            else:
                table_text.append(text[3::-1])
            text = text[4:]
        for i in sort_list:
            res += table_text[i]

    print(f'Encoded text: "{res}"')
    return res


def decode(text: str, key: str) -> str:
    """
    Returns deccoded by key text
    :param text: encoded text
    :param key: key for decoding
    :return: decoded text
    """
    old_sequence = get_reshuffle(key)
    sequence = sorted(old_sequence, key=lambda k: old_sequence[k])
    res = ""
    while len(text) > 0:
        table_text = []
        table_w = len(old_sequence)
        for i in range(0, table_w):
            table_text.append(text[:4])
            text = text[4:]
        for i in sequence:
            if old_sequence[i] % 2 == 0:
                res += table_text[i]
            else:
                res += table_text[i][::-1]

    print(f'Decoded text: "{res}"')
    return res


with open("src_text.txt", 'r', encoding='utf-8') as f:
    text = f.read()
decode(make_reshuffle("В торговом центре Москвы произошел терракт: в здание ворвались террористы.", "A very very long key for encoding"), "A very very long key for encoding")
