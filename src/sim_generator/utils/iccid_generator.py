import secrets


def generate_iccid():
    mii = "89"
    iin = "40101"
    body = ''.join(str(secrets.randbelow(10)) for _ in range(12))
    partial = mii + iin + body

    check_digit = luhn_checksum(partial)

    return partial + str(check_digit)

def luhn_checksum(partial):
    for check in range(10):
        candidate = partial + str(check)

        digits = [int(d) for d in candidate]

        for i in range(len(digits) - 2, -1, -2):
            n = digits[i] * 2
            digits[i] = n if n < 10 else n - 9

        if sum(digits) % 10 == 0:
            return check

