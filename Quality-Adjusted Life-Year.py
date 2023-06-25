num_periods_quality_life=int(input())

amount_qaly=0
for i in range(num_periods_quality_life):
    q_y=input().split()
    q=float(q_y[0])
    y=float(q_y[1])
    amount_qaly+=q*y
print("%.3f"% amount_qaly)



