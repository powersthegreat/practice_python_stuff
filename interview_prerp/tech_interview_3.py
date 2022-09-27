
small = [1,0,1]
medium = [4, 2, 1, 3, 0, 1, 2]
edge_case = [0, 2, 0]

def rainwater(histogram):
    max_wall = 0
    min_wall = 0

    for num in histogram[1:]:
        max_average = (sum(histogram[num:len(histogram)]))/(len(histogram[num:len(histogram)]))
        max_wall = max_average
        min_average = (sum(histogram[0:num]))/(len(histogram[0:num]))
        min_wall = min_average

    rain_count = ((len(histogram)/2) * max_wall) + ((len(histogram)/2) * min_wall)
    return rain_count

print(rainwater(medium))