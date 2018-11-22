import numpy


def generate_mask(i):
    mask = numpy.zeros((i, i))
    mask = mask - 1
    mask[int(i/2)][int(i/2)] = i * i - 1
    return mask


def segmentation(mask_size, image):
    mask = generate_mask(mask_size)
    [m, n] = numpy.shape(image)
    newImg = numpy.zeros([m, n])
    leftBoundary = int(mask_size/2)
    rightBoundary = leftBoundary + 1
    for i in range(leftBoundary, m-rightBoundary):
        for j in range(leftBoundary, n-rightBoundary):
            value = numpy.sum(mask * image[i-leftBoundary:i+rightBoundary, j-leftBoundary:j+rightBoundary])
            if value < 0:
                value = 0
            elif value > 255:
                value = 255

            newImg[i][j] = value
    return newImg
