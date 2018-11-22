import numpy


def generate_disk_se(radius):
    L = numpy.arange(-radius, radius + 1)
    X, Y = numpy.meshgrid(L, L)

    [m, n] = numpy.shape(X)
    se = numpy.zeros((m, n))

    for i in range(0, m):
        for j in range(0, n):
            if((X[i, j] ** 2 + Y[i, j] ** 2) <= radius ** 2):
                se[i, j] = 255

    return se


def generate_box_se(size):
    se = numpy.zeros((size, size))
    se += 255
    se = numpy.int16(se)

    return se


def hit(image):
    out = 0
    if (255 in image):
        out = 255

    return out


def fit(image):
    out = 255
    if (0 in image):
        out = 0

    return out


def dilat(mask_size, image):
    se = generate_box_se(mask_size)
    m, n = numpy.shape(image)

    leftBoundary = int(mask_size/2)
    rightBoundary = int(mask_size/2) + 1

    dilated = numpy.zeros([m, n])
    for i in range(leftBoundary, m-rightBoundary):
        for j in range(leftBoundary, n-rightBoundary):
            dilated[i][j] = hit(image[i-leftBoundary:i+rightBoundary, j-leftBoundary:j+rightBoundary])

    return dilated
