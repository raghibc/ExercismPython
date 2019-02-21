import math

def score(x, y):
    inner_dist = math.sqrt((1-0)**2+(0-0)**2)
    mid_dist = math.sqrt((5-0)**2+(0-0)**2)
    outer_dist = math.sqrt((10-0)**2+(0-0)**2)

    dart_dist = math.sqrt((x-0)**2+(y-0)**2)

    if dart_dist <= inner_dist:
        return 10
    elif inner_dist < dart_dist <= mid_dist:
        return 5
    elif mid_dist < dart_dist <= outer_dist:
        return 1
    else:
        return 0
