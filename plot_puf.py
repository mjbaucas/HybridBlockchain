from matplotlib import pyplot as plt
import numpy as np

dataX = ["1","2","4","6","8"]

#Puf Blockchain
dataPub = [0.006806667, 0.133246667, 0.976041667, 2.105966667, 2.889304167]
dataPriv = [0.004736, 0.13782, 1.11165, 1.913988889, 2.982029167]
dataHyb = [0.00707, 0.1571, 0.956841667, 2.163422222, 2.840539583]

stdPub = [0.001077201, 0.007755739, 0.045468984, 0.048591496, 0.020383902]
stdPriv = [0.000584169, 0.008986393, 0.082138459, 0.062761559, 0.057788542]
stdHyb = [0.001202777, 0.026006023, 0.032282493, 0.10091239, 0.057443611]

dataPub = np.array(dataPub)
dataPriv = np.array(dataPriv)
dataHyb = np.array(dataHyb)

stdPub = np.array(stdPub)
stdPriv = np.array(stdPriv)
stdHyb = np.array(stdHyb)


def plot_data(dataX, dataPub, dataPriv, dataHyb, name):
    plt.figure(dpi=500)
    # Plot mean lines
    plt.plot(dataX, dataPub, '-s', ms=7, color='blue', label='Public Blockchain')
    plt.plot(dataX, dataPriv, '-o', ms=7, color='orange', label='Private Blockchain')
    plt.plot(dataX, dataHyb, '-^', ms=7, color='green', label='Hybrid Blockchain')

    # Plot shaded std areas
    plt.fill_between(dataX, dataPub - stdPub, dataPub + stdPub, color='blue', alpha=0.3)
    plt.fill_between(dataX, dataPriv - stdPriv, dataPriv + stdPriv, color='orange', alpha=0.3)
    plt.fill_between(dataX, dataHyb - stdHyb, dataHyb + stdHyb, color='green', alpha=0.3)
    plt.xlabel("Number of Connected IoT Devices")
    plt.ylabel("Mean Request Completion Time (seconds)")
    plt.ylim(min(dataPriv - stdPriv) - 0.1, max(dataPriv + stdPriv) + 0.1)
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

#plot_data(dataX, dataCY, dataEY, 'responsiveness')
#plot_data(dataX, dataPub, dataPriv, 'med_block_resp')
plot_data(dataX, dataPub, dataPriv, dataHyb, 'puf_block_resp')