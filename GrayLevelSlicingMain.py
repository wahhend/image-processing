import PointProcessing as pp
import matplotlib.pyplot as pyplot

image = pyplot.imread("image/einstein.png")

stretched = pp.gray_level_slicing_preserve(image, 80, 160, 200)

figure = pyplot.figure()

figure.add_subplot(1,2,1)
pyplot.title("Original")
pyplot.imshow(image)

figure.add_subplot(1,2,2)
pyplot.title("1, 2")
pyplot.imshow(stretched)

pyplot.show()
