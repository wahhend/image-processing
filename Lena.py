import PointProcessing as pp
import matplotlib.pyplot as pyplot
import numpy

image = pyplot.imread("image/lena.png")

gray_image = pp.rgb_to_gray(image)

negative_image = pp.negative(image)

figure = pyplot.figure()
figure.add_subplot(1,3,1)
pyplot.title("Original")
pyplot.imshow(image, cmap = pyplot.get_cmap('gray'))

figure.add_subplot(1,3,2)
pyplot.title("Graysacle")
pyplot.imshow(gray_image, cmap = pyplot.get_cmap('gray'))

figure.add_subplot(1,3,3)
pyplot.title("Negative")
pyplot.imshow(negative_image)

pyplot.show()
