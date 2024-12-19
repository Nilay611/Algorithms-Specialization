def karatsuba_mult(first, second):
    if first < 10 or second < 10:
        return first * second

    size = max(len(str(first)), len(str(second))) // 2
    a, b = divmod(first, 10 ** size)
    c, d = divmod(second, 10 ** size)
    z1 = karatsuba_mult(a, c)
    z2 = karatsuba_mult(b, d)
    z3 = karatsuba_mult(a + b, c + d) - z1 - z2
    z1 *= (10 ** (2 * size))
    z3 *= (10 ** size)
    final_product = z1 + z2 + z3
    return final_product


if __name__ == "__main__":
    num1 = int(input("Enter the first no: "))
    num2 = int(input("Enter the second no: "))
    res = karatsuba_mult(num1, num2)
    print(res)
