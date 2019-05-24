import numpy as np
from PIL import Image
import os
import sys 
import scipy.misc
import matplotlib.pyplot as plt

def npy2jpg(dir,dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    file = dir
    con_arr = np.load(file) 
    for i in range(0, 182):
        arr = con_arr[i, :, :]
        disp_to_img = scipy.misc.imresize(arr, [54, 81])
        plt.imsave(os.path.join(dest_dir, "{}_disp.png".format(i)), disp_to_img, cmap='plasma')
        print('photo {} finished'.format(i))
def test(dir):
    arr = np.load(dir)
    print(arr.shape)
    # print(arr)

if __name__=="__main__":
    if sys.argv[1] == "test":
        test(sys.argv[2])
    elif sys.argv[1] == "convert":
        dir = sys.argv[2]
        dest_dir = sys.argv[3]
        npy2jpg(dir,dest_dir)
