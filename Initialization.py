import numpy as np

def str_pos(gridsize):
    z=np.zeros([gridsize,gridsize])
    z[int(gridsize/2)][int(gridsize/2)]=1
    return z

def quest(answer,gridsize):
    z=np.zeros([gridsize,gridsize+1])

    if answer==1:
        if int(gridsize/2)-20>0:
            z[int(gridsize/2)-20,:]=1
            z[int(gridsize / 2) + 20,:] = 1
            z[:,int(gridsize/2)-20]=1
            z[:,int(gridsize / 2) + 20] = 1

    if answer==2:
        for i in range(gridsize-10):
            z[i+10][gridsize-i]=1

    if answer==3:
        for i in range(gridsize):
            for k in range(gridsize):
                if ((i-int(gridsize/2)-2.5)/30)**2+((k-int(gridsize/2)-2.5)/40)**2<1:
                    z[i][k]=1

    return z


