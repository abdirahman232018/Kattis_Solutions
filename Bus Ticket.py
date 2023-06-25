#  Create array dp[n]
# ○ Define dp[i] to be minimum cost to purchase the trips 0...i
# ○ Base case: dp[0] is price of single ticket (or period ticket, if this is cheaper)
# ○ Recursive case: dp[i] is the minimum of
    # ■ buying a single ticket for the last trip: dp[i-1] + price of single trip
    # ■ buying a period ticket for the last trip: dp[j] + price of period ticket,
        # where j is the latest trip for which a
        # period ticket can not cover both trip j and trip i.




spmn=[int(item) for item in input().split()]
s,p,m,n=spmn[0],spmn[1],spmn[2],spmn[3]
days=[int(t) for t in input().split()]
def min_cost(s,p,m,days):
    n = max(days)
    days = set(days)

    dp = [0] * (n + 1)
    dp[0]=min(s,p)
    for i in range(1, n + 1):
        if i in days:
            dp[i] = min(dp[i - 1] + s, dp[i - m] + p)

        else:
            dp[i] = dp[i - 1]

    return dp[n]
print(min_cost(s,p,m,days))

spmn = [int(item) for item in input().split()]
s, p, m, n = spmn[0], spmn[1], spmn[2], spmn[3]
days = [int(t) for t in input().split()]


# def min_cost(s, p, m, days):
#     n = max(days)
#     days = set(days)
#
#     dp = [0] * (n + 1)
#     dp[0] = min(s, p)
#     for i in range(1, n + 1):
#         if i in days:
#             if i - m < 0:
#                 dp[i] = min(dp[i - 1] + s, p)
#             else:
#                 dp[i] = min(dp[i - 1] + s, dp[i - m] + p)
#
#
#         else:
#             dp[i] = dp[i - 1]
#
#     return dp[n]
#
#
# print(min_cost(s, p, m, days))
#
#
#
#
#
#
#
#
