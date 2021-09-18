import numpy as np


class TWODMAT:
    """
    This class perfoms the matrix operations to given arrays.
    """

    def nor_mat(self, arr):
        """
        Normalises a matrix of a given dimension MxN along its columns
        :param arr: matrix of shape(m,n)
        :type arr: numpy array
        :return: numpy array after manipulation
        :rtype: numpy array
        """
        # arr- a matrix of a given dimension MxN
        return np.round((arr - arr.mean(axis=0)) / arr.std(axis=0), decimals=2)

    def sum_fil(self, arr, k):
        """ 
        Implements a sum-filter of 1-d integer array of shape (n) and kernel size k

        :param arr: matrix of shape (m,n).
        :type arr: numpy array matrix
        :param k: k-top k values
        :type k: [type]
        :return: int array of shape (n+k-1)
        :rtype: numpy array matrix
        """
        # arr-array of shape (n)
        # k-kernal size
        arr = np.pad(arr, (0, k - 1), 'constant').cumsum()
        arr[k:] = arr[k:] - arr[:-k]
        return arr

    def top_pos(self, arr, k):
        """ Get the positions of top_k values of each row of a matrix of shape (m,n

        :param arr: matrix of shape (m,n).
        :type arr: numpy array matrix
        :param k: k-top k values
        :type k: [type]
        :return: int
        :rtype: numpy array matrix
        """
        # arr-a matrix of shape (m,n).
        # k-top k values
        if (arr.ndim == 1):
            arr = arr.reshape(1, -1)
        return np.fliplr(np.argsort(arr, kind='mergesort'))[:, :k]

if __name__ == '__main__':
    ''''''
    # a=TWODMAT()
    # arr= np.array([[0,0,0],[1,1,1] ,[ 2,-3,5],[-4,0,3]])
    # print(a.nor_mat(arr))
    # print(a.sum_fil(np.array([1,2,3,4,5,6]),4))
    # print(a.top_pos(np.array([[ 6,4,4,7],[ 7,8,1,0],[11,10,5,11]]),2))
