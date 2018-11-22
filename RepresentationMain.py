import matplotlib.pyplot as pyplot
import PointProcessing as pp
import MorphologicalProcessing as morph
import Segmentation as segment
import Representation as rep
import numpy
from PIL import Image

original = Image.open("image/rectangle.jpg")
original = numpy.array(original)

shifted = Image.open("image/rectangle_shifted.jpg")
shifted = numpy.array(shifted)

rotated = numpy.transpose(original)

# im = pp.rgb_to_gray(im)
ori_seg = segment.segmentation(3, original)
shift_seg = segment.segmentation(3, shifted)
rot_seg = segment.segmentation(3, rotated)

f = pyplot.figure()
f.add_subplot(3, 2, 1)
pyplot.title('original')
pyplot.imshow(original, cmap = pyplot.get_cmap('gray'))

f.add_subplot(3, 2, 2)
pyplot.title('original segmented')
pyplot.imshow(ori_seg, cmap = pyplot.get_cmap('gray'))

f.add_subplot(3, 2, 3)
pyplot.title('shifted')
pyplot.imshow(shifted, cmap = pyplot.get_cmap('gray'))

f.add_subplot(3, 2, 4)
pyplot.title('shifted segmented')
pyplot.imshow(shift_seg, cmap = pyplot.get_cmap('gray'))

f.add_subplot(3, 2, 5)
pyplot.title('rotated')
pyplot.imshow(rotated, cmap = pyplot.get_cmap('gray'))

f.add_subplot(3, 2, 6)
pyplot.title('rotated segmented')
pyplot.imshow(rot_seg, cmap = pyplot.get_cmap('gray'))

pyplot.show()

compared = rep.compare(ori_seg, shift_seg)
print("\nDiff original dan shifted : ", end="")
print( "SAMA" if compared else "BEDA")

compared = rep.compare(ori_seg, rot_seg)
print("\nDiff original dan rotated : ", end="")
print( "SAMA" if compared else "BEDA")
