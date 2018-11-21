import PointProcessing as pp
import InterImageOperation as imageopr
import matplotlib.pyplot as pyplot
import Segmentation as segment
import Representation as rep
import numpy
import PIL

im = PIL.Image.open("image/rectangle.jpg")

im = numpy.array(im)
# im = pp.rgb_to_gray(im)
im = segment.segmentation(3, im)
rotated = numpy.transpose(im)

f = pyplot.figure()
f.add_subplot(1,2,1)
pyplot.title('segmented')
pyplot.imshow(im, cmap = pyplot.get_cmap('gray'))

f.add_subplot(1,2,2)
pyplot.title('rotated')
pyplot.imshow(rotated, cmap = pyplot.get_cmap('gray'))

# pyplot.show()

print(rep.compare(im, rotated))