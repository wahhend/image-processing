import PointProcessing as pp
import matplotlib.pyplot as pyplot

image = pyplot.imread("image/baboon.png")

power_transform_2 = pp.power_law_transformation(2, image, 1)

figure = pyplot.figure()

figure.add_subplot(1,2,1)
pyplot.title("Original")
pyplot.imshow(image)

figure.add_subplot(1,2,2)
pyplot.title("1, 2")
pyplot.imshow(power_transform_2)

pyplot.show()
