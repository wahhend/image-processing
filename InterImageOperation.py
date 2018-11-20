import numpy

def substract(image1, image2):
    return image1 - image2

def bitwise_and(image1, image2):
    #return image1 & image2
    return numpy.bitwise_and(image1, image2)

def bitwise_or(image1, image2):
    #return image1 | image2
    return numpy.bitwise_or(image1, image2)

def bitwise_xor(image1, image2):
    #return image1 | image2
    return numpy.bitwise_xor(image1, image2)
