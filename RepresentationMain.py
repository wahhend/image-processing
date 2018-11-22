import matplotlib.pyplot as pyplot
import Segmentation as segment
import Representation as rep
import numpy
from PIL import Image

im = Image.open("image/rectangle.jpg")
im = numpy.array(im)
f = pyplot.figure()
f.add_subplot(1,3,1)
pyplot.title('Original')
pyplot.imshow(im, cmap = pyplot.get_cmap('gray'))

im = segment.segmentation(3, im)
rotated = numpy.transpose(im)

f.add_subplot(1,3,2)
pyplot.title('segmented')
pyplot.imshow(im, cmap = pyplot.get_cmap('gray'))

f.add_subplot(1,3,3)
pyplot.title('rotated')
pyplot.imshow(rotated, cmap = pyplot.get_cmap('gray'))

compared = rep.compare(im, rotated)
print("\nDiff original dan rotated : ", end="")
print( "SAMA" if compared else "BEDA")

pyplot.show()