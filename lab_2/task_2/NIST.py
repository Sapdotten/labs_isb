import math
import mpmath


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


if __name__ == '__main__':
    pass
