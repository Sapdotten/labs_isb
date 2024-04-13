import math
import mpmath
from typing import Union
import consts


def frequency_bitwise_test(sequence: str) -> float:
    """
    Frequency bitwise test for sequence
    :param sequence: sequence of bytes
    :return: P value
    """
    N = len(sequence)
    sum = 0
    for bit in sequence:
        if bit == '1':
            sum += 1
        else:
            sum -= 1
    P = sum / math.sqrt(N)
    P = math.erfc((P / (math.sqrt(2))))
    return P


def same_bits_test(sequence: str) -> float:
    """
    A test for the same consecutive bits in sequence
    :param sequence:  of bites
    :return: P value
    """
    sum = 0
    N = len(sequence)
    for bit in sequence:
        sum += int(bit)
    sigma = sum / N

    if not abs(sigma - 0.5) < (2 / (N ** 0.5)):
        return 0
    Vn = 0
    for i in range(0, len(sequence) - 1):
        if sequence[i] != sequence[i + 1]:
            Vn += 1
    P = math.erfc(abs(Vn - 2 * N * sigma * (1 - sigma)) / (2 * ((2 * N) ** 0.5) * sigma * (1 - sigma)))
    return P


def longest_ones_sequence_test(sequence: str) -> float:
    """
    Test for the longest sequence of units in a block
    :param sequence: sequence of bites
    :return: P value
    """
    block_lenght = 8
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    v = [0, 0, 0, 0]
    hi_2 = 0
    for block in range(0, int(len(sequence) / block_lenght)):
        max_len = 0
        curr_len = 0
        for i in range(block, block + block_lenght):
            if sequence[i] == '1':
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 0
        if max_len <= 1:
            v[0] += 1
        elif max_len == 2:
            v[1] += 1
        elif max_len == 3:
            v[2] += 1
        else:
            v[3] += 1

    for i in range(0, len(v)):
        hi_2 += ((v[i] - 16 * pi[i]) ** 2 / (16 * pi[i]))
    P = mpmath.gammainc(3 / 2, hi_2 / 2)
    return P


def read_sequence_from_file(path: str) -> Union[str, None]:
    """
    Reads a sequence from file
    :param path: path to file
    :return: sequense as str or None if can't open file
    """
    try:
        with open(path, 'r') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        return None


def sequense_test(lang: str, path_to_sequence: str) -> Union[str, None]:
    """
    Tests sequence with 3 tests
    :param lang: name of language sequence from
    :param path_to_sequence: path to file with saved sequence
    :return: result of tests as str or None if there is any error
    """
    sequence = read_sequence_from_file(path_to_sequence)
    if sequence is None:
        return None
    test1 = frequency_bitwise_test(sequence)
    test2 = same_bits_test(sequence)
    test3 = longest_ones_sequence_test(sequence)
    return f"{lang} frequency bitwise test: {test1}\n" \
           f"{lang} same consecutive bits: {test2}\n" \
           f"{lang} longest sequence of units in a block test: {test3}\n"


def save_text_to_file(text: str, path: str) -> bool:
    """
    Saves the text to file
    :param text: text to save
    :param path: path to file
    :return: true if success, false else
    """
    try:
        with open(path, 'w') as f:
            f.write(text)
        return True
    except FileNotFoundError:
        return False

def task_2() -> None:
    """
    Task 2
    :return: None
    """
    cpp_test = sequense_test('Cpp', consts.CPP_SEQUENCE_FILE)
    if cpp_test is None:
        print("Can't open file with cpp secuence")
        return None
    java_test = sequense_test('Java', consts.JAVA_SEQUENCE_FILE)
    if java_test is None:
        print("Can't open file with java secuence")
        return None
    result = java_test + cpp_test
    print(f'result is \n{result}')
    if save_text_to_file(result, consts.RESULT_FILE):
        print(f'Result has been writen to the file')
    else:
        print("Can't open file to save result")


if __name__ == '__main__':
    task_2()