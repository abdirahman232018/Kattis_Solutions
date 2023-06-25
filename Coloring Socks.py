sck=input().split()
number_of_socks, laundary_machine_capacity, max_color_diff = int(sck[0]),int(sck[1]),int(sck[2])


colors = [int(c) for c in input().split()]


colors.sort()

def number_machines(colors,number_of_socks, laundary_machine_capacity, max_color_diff):
    machines = 0
    l = 0
    while True:
        if l >= number_of_socks:
            break
        else:
            u = l + laundary_machine_capacity - 1

            if u >= number_of_socks:
                u = number_of_socks - 1
            while u >= l:
                if colors[u] - colors[l] <= max_color_diff:
                    machines += 1
                    l = u + 1
                    break
                u -= 1

    return machines
if number_of_socks<=laundary_machine_capacity:
    print(1)
else:
    print(number_machines(colors,number_of_socks, laundary_machine_capacity, max_color_diff))