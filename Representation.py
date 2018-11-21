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
        # print(current)
    return representation


def nol(akhir):
    switcher = {
        0: 0,
        1: 1,
        2: 2,
        3: 3
    }
    return switcher.get(akhir, 0)


def satu(akhir):
    switcher = {
        0: 3,
        1: 0,
        2: 1,
        3: 2
    }
    return switcher.get(akhir, 0)


def dua(akhir):
    switcher = {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }
    return switcher.get(akhir, 0)


def tiga(akhir):
    switcher = {
        0: 1,
        1: 2,
        2: 3,
        3: 0
    }
    return switcher.get(akhir, 0)


def diff(current, next):
    switcher = {
        0: nol(next),
        1: satu(next),
        2: dua(next),
        3: tiga(next),
    }
    return switcher.get(current, )


def compare(source, image):
    originalChainCode = represent_4_direction(source)
    rotatedChainCode = represent_4_direction(image)

    originalDiff = [diff(originalChainCode[i], originalChainCode[i+1])
                    for i in range(0, len(originalChainCode)-1)]
    rotatedDiff = [diff(rotatedChainCode[i], rotatedChainCode[i+1])
                   for i in range(0, len(rotatedChainCode)-1)]

    originalDiff.append(diff(originalChainCode[len(originalChainCode) - 1], originalChainCode[0]))
    rotatedDiff.append(diff(rotatedChainCode[len(rotatedChainCode) - 1], rotatedChainCode[0]))

    sourceDiff = originalDiff + originalDiff
    originalDiffCode = ""
    rotatedDiffCode = ""

    for code in sourceDiff:
        originalDiffCode += str(code)
    for rd in rotatedDiff:
        rotatedDiffCode += str(rd)

    return (rotatedDiffCode in originalDiffCode)
