import numpy as np

def avada_kedavara(my_list):
    """
    Doing as directed in the question.
    Removing comments for because of indemtation errors encountered while executing the code
    
    :param my_list: a list of 25 integers
    :param a0: 1D numpy array of 25 elements
    :param a1: 5 X 5 numpy matrix
    :param a1cpy: copy of a1 matrix
    
    """
    a0 = np.array(my_list)
    print("a0 at beginning:\n{}".format(a0))
    a1 = a0.reshape(5,5)
    print("a1 at the beginning:\n{}".format(a1))
    a1[2,2] = 0
    print("a1 after change:\n{}".format(a1))
    print("a0 after changing a1:\n{}".format(a0))
    print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")
    a1cpy = a1.copy().flatten()
    a1cpy = np.round_(a1cpy*(0.7) , decimals =2)
    print("a1cpy\n{}".format(a1cpy))
    print("a1 after changing its copy:\n{}".format(a1))
 

def incendio(my_integer):
    """
    Doing as directed in the question.
    Removing comments for because of indemtation errors encountered while executing the code
    
    :param my_integer: an even integers
    :param arng0: numpy array
    :param arng1: numpy array
    :param mult0: numpy array
    """
    arng0 = np.arange(my_integer,4*my_integer,2)
    arng0 = arng0.reshape(3,2)
    print("arng0\n{}".format(arng0))
    arng1 = np.arange(my_integer,12+my_integer)
    arng1 = np.reshape(arng1,(4,3),order='F')
    print("arng1\n{}".format(arng1))
    mult0 = np.dot(arng0.T, arng1.T)
    print("mult0\n{}".format(mult0))
    v0 = mult0.min(axis=1)
    print("shape of v0: \n{}".format(v0.shape))
    v0 = v0.reshape(v0.shape[0],1)
    base0 = np.subtract(mult0, v0)
    print("base0\n{}".format(base0))
    base0 = np.square(base0)
    ans = np.sum(base0)
    print("ans : {}".format(ans))


def reducio(X, W):
    """
    Performing Batch Matrix Multiplication
    
    :param X: Three dimensional matrix with shape => {B,S,F}
    :param W: Two dimensional matrix with shape => {N,F}
    
    :return: numpy matrix after performing batch matrix multiplication and transforming to shape {B,N,S}
    
    """
    return np.einsum('ijk,kl->ilj',X, W.T)



def alohomora(n, m):
    """
    Constructing a checkerboard pattern matrix of dimension NxN which considers each block of dimension MxM as a cell for the pattern.
    
    :param n: integers
    :param m: integer that divides n
    
    :return: int numpy Ndarray
    :dim: n X n
    """
    checkerboard = np.zeros((n,n))
    for i in range(0,n,m):
        for j in range(0,n,m):
            if(i/m)%2==0:
                if(j/m)%2==0:
                    checkerboard[i:i+m,j:j+m]= np.ones((m,m))
            elif(i/m)%2!=0:
                if(j/m)%2!=0:
                   checkerboard[i:i+m,j:j+m]= np.ones((m,m)) 
    checkerboard = checkerboard.astype('int')
    #print(checkerboard)
    return checkerboard
    
    
def glisseo(P,Q,R,S):
    """
    :param p: string
    :param q: string
    :param r: string
    :param s: string
    :param P: string
    :param Q: string
    :param R: string
    :param S: string
    
    :return: numpy matrix in the form [[P`,Q`],[R`,S`]]
    """
    p = np.matrix(P)
    q = np.matrix(Q)
    r = np.matrix(R)
    s = np.matrix(S)
    
    main_matrix = np.vstack((np.c_[p,q],np.c_[r,s]))
    
    #print("main matrix:\n{}".format(main_matrix))
    return main_matrix
    

def expelliarmus(arr, theta, axis):
    """
    :param arr : float Ndarray
    :dim: Nx3
    :param theta: float; 0≤theta<360 (in degrees)
    :param axis: str; axis ∈ {'X','Y','Z'}
    
    :return type: float Ndarray
    :dim: N X 3
    
    """
    if axis == 'X':
        angle = np.matrix([[ 1, 0 , 0 ],[ 0, np.cos(np.radians(theta)),-np.sin(np.radians(theta))],[0, np.sin(np.radians(theta)), np.cos(np.radians(theta))]])
        arr = np.dot(angle,arr.T)
        arr = np.round_(arr.T, decimals = 2)
    if axis == 'Y':
        angle = np.matrix([[np.cos(np.radians(theta)),0,np.sin(np.radians(theta))],[0,1,0],[-np.sin(np.radians(theta)), 0, np.cos(np.radians(theta))]])
        arr = np.dot(angle,arr.T)
        arr = np.round_(arr.T, decimals = 2)
    if axis == 'Z':
        angle=np.matrix([[np.cos(np.radians(theta)), -np.sin(np.radians(theta)), 0 ],[np.sin(np.radians(theta)),np.cos(np.radians(theta)),0],[0 ,0,1]])
        arr = np.dot(angle, arr.T)
        arr = np.round_(arr.T, decimals = 2)
        
    #print(arr)
    return arr