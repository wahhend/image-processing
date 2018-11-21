import numpy

def rgb_to_gray(image):
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]

    #gray = (numpy.max(red, green, blue) + numpy.min(red, green, blue)) / 2
    # gray = (red + green + blue)/3
    gray = 0.21*red + 0.71*green + 0.07*blue

    return gray


def negative(image):
    #max = numpy.max(image)
    max = 1
    negative = max - image

    return negative


def log_transformation(const, image):
    #image = 255 * image
    log_transform =  const * numpy.log10(1+image)

    return log_transform


def power_law_transformation(const, image, power):
    power_transform = const * image ** power

    return power_transform


def contrast_stretching(image, points):
    lines = find_line(points)
    base = [point[0] for point in points]
    base.append(255)
    
    image = 255 * image

    image_dimension = numpy.shape(image)

    for i in range(image_dimension[0]):
        for j in range(image_dimension[1]):
            if len(image_dimension) == 3:
                for k in range(image_dimension[2]):
                    image[i][j][k] = map_pixels(base, lines, image[i][j][k])
            else:
                image[i][j] = map_pixels(base, lines, image[i][j])
    
    image = image / 255

    return image

def find_line(points):
    points.append([255, 255])
    x, y = 0, 0
    lines = list()

    for point in points:
        if point[0] - x == 0:
            gradient = 0
        else:
            gradient = (point[1] - y)/(point[0] - x)
        c = gradient * point[0] * -1 + point[1]
        
        lines.append([gradient, c])

        x = point[0]
        y = point[1]

    return lines


def map_pixels(base, lines, value):
    for i in range(len(base)):
        if value < base[i]:
            return lines[i][0] * value + lines[i][1]


def gray_level_slicing_lower(image, start, stop, high, low):
    image = 255 * image
    image = numpy.where((image > start) & (image < stop), high, low)
    image = image / 255

    return image

def gray_level_slicing_preserve(image, start, stop, high):
    image = 255 * image
    image = numpy.where((image > start) & (image < stop), high, image)
    image = image / 255

    return image


def bit_plane_slicing(image, index):
    image = rgb_to_gray(image)
    image = 255 * image
    image = numpy.uint8(image)
    image_dimension = numpy.shape(image)
    
    for i in range(image_dimension[0]):
        for j in range(image_dimension[1]):
            image[i, j] = numpy.unpackbits(image[i,j])[index-1]
    
    return image
