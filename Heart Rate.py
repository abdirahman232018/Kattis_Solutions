n=int(input())

for i in range(n):
    b_p=input().split()
    b=float(b_p[0])
    p=float(b_p[1])

    bpm=(60*b)/p
    abpm=60/p
    max_bpm=bpm+abpm
    min_bpm=bpm-abpm
    print("%.4f" % min_bpm,"%.4f" % bpm,"%.4f" % max_bpm)

