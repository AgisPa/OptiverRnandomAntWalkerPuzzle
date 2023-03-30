
import numpy as np

dict={
    1:"Moves Left",
    2:"Moves Right",
    3:"Moves Up",
    4:"Moves Down"
}
def rndwalk(z0):
    a=np.random.randint(1,5)
    z=np.zeros([len(z0),len(z0)])
    if 1 in z0:
        i = np.where(z0 == 1)[0][0]
        k = np.where(z0 == 1)[1][0]
        if dict[a]=="Moves Left" and k-10>0:
            z[i][k-10]=1
        if dict[a]=="Moves Right" and k+10<len(z0):
            z[i][k+10]=1
        if dict[a]=="Moves Up" and i+10<len(z0):
            z[i+10][k]=1
        if dict[a]=="Moves Down" and i-10>0:
            z[i-10][k]=1
    return z




