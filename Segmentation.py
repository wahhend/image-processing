import numpy


def generate_mask(i):
    mask = numpy.zeros((i, i))
    mask = mask - 1
    mask[int(i/2)][int(i/2)] = i * i - 1
    return mask


def segmentation(mask, image):
    mask = generate_mask(mask)
    [m, n] = numpy.shape(image)
    newImg = numpy.zeros([m, n])

    for i in range(1, m-2):
        for j in range(1, n-2):
            value = numpy.sum(mask * image[i-1:i+2, j-1:j+2])
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            
            newImg[i][j] = value
    return newImg
