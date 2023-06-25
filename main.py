#Geometry
def get_euclidian_distance(p1,p2):
    pass


#Mathematics

def gcd(a,b):
    while b:
        r=a%b
        a=b
        b=r
    return a
def lcm(a,b):
    return a*(b/(gcd(a,b)))
def getPrimes(num):
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)
def dp_get_nth_fb(n):
    if n==1:
        return 0
    a,b=1,1
    for i in range(3,n):
        c=a+b
        a=b
        b=c
    return b
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
def binomial_cofficient(n,k):
    if n==k or k==0:
        return 1
    return factorial(n)/(factorial(k)*factorial(n-k))
def floy_find_cycle():
    pass



if __name__ == '__main__':
    import math

    for i in range(1,100):
        pow0=(-i*(i-1))/730
        pn = math.exp(pow0)
        pn_2=1-pn
        if round(pn_2,2)==0.99:
            print(i)






    
