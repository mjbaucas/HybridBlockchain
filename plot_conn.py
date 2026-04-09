from matplotlib import pyplot as plt
import numpy as np

dataX = ["1","2","4","6","8"]

#Puf Blockchain
dataPriv = [0, 90.5, 657.33, 1199.4, 1524.5]
dataPub = [0, 252.5, 831.92, 1310.6, 4096.2]
dataNo = [0, 41.33, 567.75, 1214.6, 1531.5]


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
    plt.ylabel("Average number of connection resets")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)


plot_data(dataX, dataPub, dataPriv, dataNo, 'comp_conn')