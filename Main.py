__author__ = "Agisilaos Papatheodorou"
__copyright__ = "Copyright (C) 2023 Agisilaos Papatheodorou"
__license__ = "Public Domain"
__version__ = "1.0"


import MainExecutable

#Results for 1000 iterations on question 1: 5.418 seconds

#Results for 1000 iterations on question 2: 6.927 seconds

#Results for 1000 iterations on question 3: 14.716 seconds

#For questions 1,2,3 input the corresponding number as the answer variable

answer=1

#Suggested grid size
gridsize=100

time=list()

#Number of iterations
ite=10

#Toggle visuals on or off
vis=True

for i in range(ite):
    time.append(MainExecutable.exe(gridsize,answer,vis))
    while "null" in time:
        time.remove("null")
print("Average time:",sum(time)/ite, "seconds")