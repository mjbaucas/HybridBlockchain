def read_sram(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    sram_data = {}
    for line in lines:
        line = line.strip()
        temp = line.split(" ")
        data = temp[1].split(",")
        sram_data[temp[0]] = data

    return(sram_data)
