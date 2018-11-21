import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as image
import Segmentation as sg
import Representation as rp
import PointProcessing as pp


im = image.open("image/rectangle.jpg")

f = plt.figure()
f.add_subplot(1,2,1)
plt.title('original')
plt.imshow(im)

im = np.array(im)
# im = pp.rgb_to_gray(im)
im = sg.segmentation(3, im)

im = np.transpose(im)

f.add_subplot(1,2,2)
plt.title('segmentation')
plt.imshow(im, cmap = plt.get_cmap('gray'))

plt.show()

def nol(akhir):
    switcher = {
        0: 0,
        1: 1,
        2: 2,
        3: 3
    }
    return switcher.get(akhir, 0)

def satu(akhir):
    switcher = {
        0: 3,
        1: 0,
        2: 1,
        3: 2
    }
    return switcher.get(akhir, 0)

def dua(akhir):
    switcher = {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }
    return switcher.get(akhir, 0)
def tiga(akhir):
    switcher = {
        0: 1,
        1: 2,
        2: 3,
        3: 0
    }
    return switcher.get(akhir, 0)

def dif (awal, akhir) :
    switcher = {
        0 : nol(akhir),
        1 : satu(akhir),
        2 : dua(akhir),
        3 : tiga(akhir),
    }
    return switcher.get(awal, "salah")

code = rp.represent_4_direction(im)
# code = list(map(int, code))
diff = [ dif(code[i],code[i+1]) for i in range(0, len(code)-1)]
diff.insert(0,3)
print("Code :", code)
print("Diff :",diff)