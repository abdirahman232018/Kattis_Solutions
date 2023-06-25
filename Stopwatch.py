num_pressed=int(input())


if num_pressed%2==1:
    still_running = "still running"
    for i in range(num_pressed):
        t2 = int(input())
    print(still_running)
else:
    time_passed = 0
    for i in range (int(num_pressed/2)):
        t1 = int(input())
        t2=int(input())
        diff=t2-t1
        time_passed+=diff
    print(time_passed)






