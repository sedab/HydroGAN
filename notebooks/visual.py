import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
import h5py
import matplotlib as mpl
%matplotlib inline
import itertools

## load file
f = h5py.File("sample16.h5", mode="r")
f = np.array([*f["sample16"]])

## function for truncating the colormap
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    """Function for dividing cmaps,
    Retrieved from: https://stackoverflow.com/questions/\
    18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib"""
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

import itertools
cube_size = 128
random_cube_index = 0
stdev_mask = 1
edge = np.array([*range(cube_size)])

fig = plt.figure(figsize=(20,20)) 
ax = fig.add_subplot(111, projection='3d') 

start = random_cube_index
end = random_cube_index+cube_size
    
data_value = f[0][start:end,
                  start:end,
                  start:end]

x,y,z = edge,edge,edge

product = [*itertools.product(x,y,z)]

X = np.array([product[k][0] for k in [*range(len(product))]])
Y = np.array([product[k][1] for k in [*range(len(product))]])
Z = np.array([product[k][2] for k in [*range(len(product))]])

data_1dim = np.array([data_value[X[i]][Y[i]][Z[i]] for i in [*range(len(product))]])
initial_mean = np.mean(data_1dim) - 2*np.std(data_1dim)
mask = data_1dim > 0
mask = mask.astype(np.int)

data_1dim = np.multiply(mask,data_1dim)
X = X[np.where(data_1dim>0)]
Y = Y[np.where(data_1dim>0)]
Z = Z[np.where(data_1dim>0)]
data_1dim = data_1dim[np.where(data_1dim>0)]
s = 600*data_1dim/np.linalg.norm(data_1dim)

cmap=plt.get_cmap("Blues")
new_cmap = truncate_colormap(cmap, 0.96, 1,n=1000)

print (s[:5])
ax.scatter(X, Y, Z, 
           c=data_1dim, 
           cmap=new_cmap,
           s=s,alpha=1)
plt.show()