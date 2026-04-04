import random

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

def pick_crp(sram_data):
    random_address = random.choice(list(sram_data.keys()))
    random_row = random.randint(0, len(sram_data[random_address]))

    return random_address, random_row

def match_crp(sram_data, sram_address, row_address, response)
    return sram_data[sram_address][row_address] == response