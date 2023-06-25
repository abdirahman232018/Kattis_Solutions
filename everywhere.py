T=int(input())

for i in range(T):
    num_trips=int(input())
    dist_cities=set()
    for j in range(num_trips):
        trip=input()
        dist_cities.add(trip)
    print(len(dist_cities))
