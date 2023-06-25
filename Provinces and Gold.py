line=input().split()
gold,silver,copper=int(line[0]),int(line[1]),int(line[2])
victory_cots={"Province":8,"Duchy":5,"Estate":2}
tresur_costs={"gold":6,"silver":3,"copper":0}

vic_points={"Province":6,"Duchy":3,"Estate":1}


points=(gold*3)+(silver*2)+(copper)
if points==1:
    print("Copper")
elif points==2:
    print("Estate or Copper")
elif points==3 or points==4:
    print("Estate or Silver")
elif points==5:
    print("Duchy or Silver")
else:
    print("Province or Gold")


