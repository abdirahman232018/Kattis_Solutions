
n,h,v=list(map(int,input().split()))

bigger_upper=max(h*v,(n-v)*h)
bigger_lower=max((n-v)*(n-h),(n-h)*v)
max_area=max(bigger_upper,bigger_lower)
print(max_area*4)