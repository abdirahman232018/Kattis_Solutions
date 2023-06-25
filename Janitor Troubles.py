import math
s1,s2,s3,s4=list(map(int, input().split()))
s=(s1+s2+s3+s4)/2 #half perimeter

max_area = math.sqrt(((s - s1) * (s - s2) * (s - s4) * (s - s4)))
print("%.6f"%max_area)






