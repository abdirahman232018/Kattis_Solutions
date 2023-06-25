import math

def find_nearest_convenient_plot(r):
    # Find the nearest convenient plot by finding the largest x and y
    # coordinates that are less than or equal to the radius 'r'

    # Calculate the floor of 'r' to ensure that the plot is outside the Disc District
    x = math.floor(r)
    y = math.floor(r)

    return x, y

# Read the radius 'r' from the input
r = int(input())

# Find the nearest convenient plot
x, y = find_nearest_convenient_plot(r)

# Output the result
