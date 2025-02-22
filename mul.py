

def mul(a, b):

    la = len(a)

    lb = len(b)


    if la <= 10 or lb <= 10:

        return int(a) * int(b)


    if la > lb:

        b = b.rjust(la, '0')

        l = la

    else:

        a = a.rjust(lb, '0')

        l = lb


    m = l // 2

    h1, l1 = a[:m], a[m:]

    h2, l2 = b[:m], b[m:]


    ph = mul(h1, h2)

    pl = mul(l1, l2)

    pm = mul(h1, l2) + mul(l1, h2)


    return (10 ** l) * ph + (10 ** m) * pm + pl


# ورودی دو عدد

num1 = input()

num2 = input()



r = mul(num1, num2)

print(r)
