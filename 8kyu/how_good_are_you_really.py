# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
########################################################################


def better_than_average(class_points, your_points):
    i = 0
    sum = 0
    while i < len(class_points):
        sum += class_points[i]
        i += 1
    print(sum)
    total_points = sum + your_points
    class_avg = total_points/ (len(class_points) + 1)
    if class_avg > your_points:
        return False
    else:
        return True

print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))

