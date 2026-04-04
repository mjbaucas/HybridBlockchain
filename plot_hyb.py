from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8"]

#Hyb Blockchain
dataPub = [4.438865, 9.275252, 19.48161, 28.48011, 47.26013]
dataPriv = [0.005249, 0.120771, 1.204335, 1.981195, 2.614513]
dataHyb = [4.456061, 9.243036, 19.45907, 29.06414, 48.55915]


def plot_data(dataX, dataPub, dataPriv, dataHyb, name):
    plt.figure(dpi=500)
    plt.plot(dataX,dataPub,marker='s', ms=8, label="Public Blockchain", color="blue")
    plt.plot(dataX,dataPriv,marker='o', ms=8,label="Private Blockchain", color="orange")
    plt.plot(dataX,dataHyb,marker='^', ms=8,label="Hybrid Blockchain", color="green")
    plt.xlabel("Number of Connected IoT Devices")
    plt.ylabel("Average Request Completion Time (seconds)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

plot_data(dataX, dataPub, dataPriv, dataHyb, 'hyb_block_resp')