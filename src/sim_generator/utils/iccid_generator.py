import secrets


def generate_iccid():
    mii = "89"
    body = ''.join(str(secrets.randbelow(10)) for _ in range(17))
    partial = mii + body

    check_digit = luhn_checksum(partial)

    return partial + str(check_digit)

def luhn_checksum(digits: str) -> int:
    total = 0
    reverse_digits = digits[::-1]

    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return (10 - (total % 10)) % 10