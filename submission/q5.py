import numpy as np
import sys
from matplotlib import pyplot as plt


def normalize(data, minI, maxI, minO, maxO):
    """
    Attempts to improve an image by stretching the range of intensity values it contains to make full use of possible values 
    Following formula is used to perform constract strecting.

    s = (s-c)*(b-a)/(d-c) + a   (linear mapping so get equation of a straight line)

    where s = new constract value
    These lower and upper limits will be called a and b, respectively (for standard 8-bit grayscale pictures, these limits are usually 0 and 255)
    The value limits (lower = c, upper = d) in the unmodified picture

    :param data: numpy array of image
    :type data: ndarray
    :param minI: lower limit of unmodified data
    :type minI: int
    :param maxI: upper limit of unmodified data
    :type maxI: int
    :param minO: lower limit of standard picture which is 0
    :type minO: int
    :param maxO: upper limit of standard picture which is 255
    :type maxO: int


    :return: normalized numpy ndarray.
    :rtype: ndarray
    """
    return np.multiply((data-minI), (((maxO-minO)/(maxI-minI))+minO))


# write your code here!
if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--data", nargs="+")
    if(len(sys.argv) > 1 and sys.argv[1] == '--data'):
        file = sys.argv[2]
        data = np.load(file)
        data = normalize(data, data.min(), data.max(), 0, 255)
        plt.imsave('q5_result.png', data.astype('uint8'))
        plt.imshow(data)
    else:
        raise ValueError("Missing --data option")
