mon_date1=input().split(" ")
mon=mon_date1[0]
date1=mon_date1[1]
if (mon == "OCT" and date1=="31") or (mon == "DEC" and date1=="25"):
    print("yup")
else:
    print("nope")
