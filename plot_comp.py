from matplotlib import pyplot as plt
import numpy as np

dataX = ["1","2","4","6","8"]

#Puf Blockchain
dataPriv = [0.0061, 0.066, 1.0402, 1.8863, 3.0836]
dataPub = [4.5019, 9.4593, 19.697, 30.079, 43.534]
dataNo = [0.0079, 0.0337, 1.1, 2.1623, 3.2752]


dataPub = np.array(dataPub)
dataPriv = np.array(dataPriv)
dataNo = np.array(dataNo)

def plot_data(dataX, dataPub, dataPriv, dataNo, name):
    plt.figure(dpi=500)
    # Plot average lines
    plt.plot(dataX, dataPub, '-D', ms=6, color='purple', label='Public Blockchain')
    plt.plot(dataX, dataPriv, '-s', ms=6, color='teal', label='Private Blockchain')
    plt.plot(dataX, dataNo, '-*', ms=9, color='red', label='No Blockchain', alpha=0.85)
    
    plt.xlabel("Number of connecting devices")
    plt.ylabel("Average request completion time (seconds)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

plot_data(dataX, dataPub, dataPriv, dataNo, 'comp_resp')