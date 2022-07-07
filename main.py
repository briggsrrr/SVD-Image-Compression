import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
import cv2

from mpl_toolkits.mplot3d import axes3d


def compress(cf):
    # Read the image from a .jpg file and get just the black intensity of each pixel
    img = plt.imread('Leaf.jpg')


    M = np.float64(img[:,:,0])
    nrows, ncols = M.shape
 
    U, sigma, Vt = npla.svd(M, full_matrices=False)
    
    nrows, ncols = M.shape
    Mstorage = nrows*ncols
 
    k = Mstorage/(cf*(nrows+ncols))
    
    Mstorage = nrows*ncols
    Mkstorage = k * (nrows+ncols)
    
    Mk = np.zeros(M.shape)
    for i in range(round(k)):
        Mk += sigma[i] * np.outer(U[:,i], Vt[i,:])
    
   
    # plot the original image in matrix M
    plt.figure(1,figsize=(10,10))
    plt.imshow(M, cmap = "gray")
    plt.title('Original Image')
    # plot the compressed image in matrix Mk
    plt.figure(2,figsize=(10,10))
    plt.imshow(Mk, cmap = "gray")
    plt.title('Compressed Image')
    plt.show()

    print("Sucessfully created both windows.")


def main(): 
    compress(5)

main()