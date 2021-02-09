def monotone_increasing_digits(n):
    result = 0
    n_power = 1

    while n > 0:
        digit = n % 10
        n //= 10
        high = n % 10
        if high > digit:
            result = n_power * 10 - 1
            n -= 1
        else:
            result += digit * n_power
        n_power *= 10
    return result


def monotone_increasing_digits2(n):
    char_list = list(str(n))
    max = -1
    idx = -1
    for x in range(0, len(char_list)):
        if max < int(char_list[x]):
            max = int(char_list[x])
            idx = x
        if x + 1 < len(char_list) and int(char_list[x]) > int(char_list[x + 1]):
            char_list[idx] = str(int(char_list[idx]) - 1)
            for j in range(idx + 1, len(char_list)):
                char_list[j] = '9'
            break
    return int("".join(char_list))


if __name__ == '__main__':
    monotone_increasing_digits(1)
