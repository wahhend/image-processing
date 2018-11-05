import PointProcessing as pp
import matplotlib.pyplot as pyplot

image = pyplot.imread("image/einstein.png")

gray_image = pp.rgb_to_gray(image)
log_transform_02 = pp.log_transformation(0.5, image)
log_transform_07 = pp.log_transformation(5, image)

figure = pyplot.figure()

figure.add_subplot(1,3,1)
pyplot.title("Original")
pyplot.imshow(image)

figure.add_subplot(1,3,2)
pyplot.title("0.5")
pyplot.imshow(log_transform_02, cmap = pyplot.get_cmap('gray'))

figure.add_subplot(1,3,3)
pyplot.title("5")
pyplot.imshow(log_transform_07,  cmap = pyplot.get_cmap('gray'))

pyplot.show()