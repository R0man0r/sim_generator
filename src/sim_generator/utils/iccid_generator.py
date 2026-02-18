import secrets


def generate_iccid():
    mii = "89"
    iin = "40102"
    body = ''.join(str(secrets.randbelow(10)) for _ in range(12))
    partial = mii + iin + body

    check_digit = luhn_checksum(partial)

    return partial + str(check_digit)

def luhn_checksum(digits: str) -> int:
    total = 0
    reverse_digits = digits[::-1]

    for i, d in enumerate(reverse_digits):
        n = int(d)

        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9

        total += n

    return (10 - (total % 10)) % 10

