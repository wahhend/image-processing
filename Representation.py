import numpy


def find_start(image):
    size = numpy.shape(image)
    for i in range(size[0]):
        for j in range(size[1]):
            if image[i][j] > 128:
                return[i, j]

def represent_4_direction(image):
    representation = []
    trace = []
    start = find_start(image)
    return_to_start = False
    current = [start[0], start[1]]
    while(not return_to_start):
        if image[current[0]][current[1]+1] > 128 and [current[0], current[1]+1] not in trace:
            representation.append(0)
            current[1] += 1
            trace.append([current[0], current[1]])

        elif image[current[0]-1][current[1]] > 128 and [current[0]-1, current[1]] not in trace:
            representation.append(1)
            current[0] -= 1
            trace.append([current[0], current[1]])

        elif image[current[0]][current[1]-1] > 128 and [current[0], current[1]-1] not in trace:
            representation.append(2)
            current[1] -= 1
            trace.append([current[0], current[1]])

        elif image[current[0]+1][current[1]] > 128 and [current[0]+1, current[1]] not in trace:
            representation.append(3)
            current[0] += 1
            trace.append([current[0], current[1]])

        return_to_start = (start == current)
        print(current)
    return representation


