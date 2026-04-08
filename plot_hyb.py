from matplotlib import pyplot as plt
import numpy as np

dataX = ["1","2","4","6","8"]

#Puf Blockchain
dataPriv = [0.00525, 0.12077, 1.20434, 1.9812, 2.61451]
dataPub = [4.43887, 9.27525, 19.4816, 28.4801, 47.2601]
dataHyb = [0.45615, 1.10941, 3.22316, 5.57642, 6.57472]
dataNo = [0.00907, 0.08358, 1.09776, 2.307, 2.77893]

stdPriv = [0.00053, 0.21015, 0.46051, 1.22827, 1.28253]
stdPub = [0.00876, 0.41707, 1.60829, 1.57993, 12.0961]
stdHyb = [0.00499, 0.49598, 0.66698, 2.1203, 0.97057]
stdNo = [0.00054, 0.15973, 0.61723, 1.02884, 0.48083]

dataPub = np.array(dataPub)
dataPriv = np.array(dataPriv)
dataHyb = np.array(dataHyb)
dataNo = np.array(dataNo)

stdPub = np.array(stdPub)
stdPriv = np.array(stdPriv)
stdHyb = np.array(stdHyb)
stdNo = np.array(stdNo)


def plot_data(dataX, dataPub, dataPriv, dataHyb, dataNo, name):
    plt.figure(dpi=500)
    # Plot mean lines
    plt.plot(dataX, dataPub, '-^', ms=7, color='red', label='Public Blockchain')
    plt.plot(dataX, dataPriv, '-D', ms=7, color='blue', label='Private Blockchain')
    plt.plot(dataX, dataHyb, '-s', ms=7, color='orange', label='Hybrid Blockchain')
    plt.plot(dataX, dataNo, '-o', ms=7, color='green', label='No Blockchain')


    # Plot shaded std areas
    plt.fill_between(dataX, dataPub - stdPub, dataPub + stdPub, color='red', alpha=0.3)
    plt.fill_between(dataX, dataPriv - stdPriv, dataPriv + stdPriv, color='blue', alpha=0.3)
    plt.fill_between(dataX, dataHyb - stdHyb, dataHyb + stdHyb, color='orange', alpha=0.3)
    plt.fill_between(dataX, dataNo - stdNo, dataNo + stdNo, color='green', alpha=0.3)
    
    plt.xlabel("Number of connecting devices")
    plt.ylabel("Mean request completion time (seconds)")
    #plt.ylim(min(dataPriv - stdPriv) - 0.1, max(dataPriv + stdPriv) + 0.1)
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

#plot_data(dataX, dataCY, dataEY, 'responsiveness')
#plot_data(dataX, dataPub, dataPriv, 'med_block_resp')
plot_data(dataX, dataPub, dataPriv, dataHyb, dataNo, 'block_resp')