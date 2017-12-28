# -*- coding: utf-8 -*-


def get_check_code(fcode):
    """
    Get final check digit with mod 11, 10 encryption algorithm
    :param fcode: top 14 digits of registration number
    :type fcode: str or list of int
    :return: final check digit
    :rtype: int
    """
    fcode = list(map(int, fcode))
    assert len(fcode) == 14, "Inputted fcode should be 14 digits."
    p = 10
    for i in range(14):
        p = p % 11
        if p == 0: p = 11
        s = p + fcode[i]
        s = s % 10
        if s == 0: s = 10
        p = s * 2
        # print(i, fcode[i], s, p)
    p = p % 11
    if p <= 1:
        a1 = 1 - p
    else:
        a1 = 11 - p
    return str(a1)


if __name__ == '__main__':
    origin_code = '110108012660422'
    fcode = origin_code[0:14]
