def flip_backward(digits):
    d = ""
    for i in range(len(digits) - 1, 0, -1):
        d += digits[i]
    d+=digits[0]
    return int(d)


def compare_two_num(a, b):
    if a >= b:
        return a
    return b

AB=input().split()

A=flip_backward(AB[0])
B=flip_backward(AB[1])
print(compare_two_num(A,B))