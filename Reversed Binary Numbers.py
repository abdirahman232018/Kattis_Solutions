def convert_binary(n):
    bits=bin(n)
    return bits[2::]
def reverse_bits(bits):
    return bits[::-1]

def convert_decimal(bin_str):
    res=0
    j=len(bin_str)-1
    for b in bin_str:
        if b=="1":
            res+=2**j
        j-=1
    return res

N=int(input())
#convert to binary
b=convert_binary(N)
#reverse
r=reverse_bits(b)
#convert to decimal
d=convert_decimal(r)
print(d)


