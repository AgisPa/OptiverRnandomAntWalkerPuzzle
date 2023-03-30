# This is the Python script for the Optiver Graduate Quantatative Researcher Puzzle.

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import Initialization
import Movement
import numpy as np

gridsize=100
answer=2

def exe(gridsize,answer,vis):
    z0=Initialization.str_pos(gridsize)

    stop=True
    seconds=0


    while stop:
        if seconds==0:
            z=z0
        else:
            z = Movement.rndwalk(z)
        seconds += 1
        q=Initialization.quest(answer,gridsize)

        if 1 in z:
            i = np.where(z == 1)[0][0]
            k = np.where(z == 1)[1][0]
        else:
            stop=False
            seconds = "null"

        if q[i][k]==1 and (answer==1 or answer==2):
            stop=False
            print("The ant took", seconds, "seconds to find food.")

        elif answer==3 and ((i-int(gridsize/2)-2.5)/30)**2+((k-int(gridsize/2)-2.5)/40)**2>1:
            stop = False
            print("The ant took", seconds, "seconds to find food.")

        if vis:
            fig, ax = plt.subplots(figsize=(10, 8))
            a = ax.contour(z, cmap="Reds", alpha=.5, zorder=5, extend='max')

            ax.contour(q, cmap="Greens", alpha=.5, zorder=5, extend='max')

            red_patch = mpatches.Patch(color='red', label='Ant Position')
            green_patch = mpatches.Patch(color='green', label='Food Position')
            ax.legend(handles=[green_patch, red_patch])

            ax.set_xticks(np.linspace(0, gridsize, 11, dtype=int))
            ax.set_xticklabels(np.linspace(-int(gridsize / 2), int(gridsize / 2), 11, dtype=int))
            ax.set_xlabel("South")

            ax.set_yticks(np.linspace(0, gridsize, 11, dtype=int))
            ax.set_yticklabels(np.linspace(-int(gridsize / 2), int(gridsize / 2), 11, dtype=int))
            ax.set_ylabel("West")

            ax.xaxis.grid(True, zorder=0)
            ax.yaxis.grid(True, zorder=0)

            ax.tick_params(labeltop=True, labelright=True)

            ax2 = ax.twinx()

            ax2.set_ylabel('East')
            ax2.set_xlabel('North')

            plt.ion()
            plt.show()
            plt.pause(0.6)
            plt.close()


    return seconds

