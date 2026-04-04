from sram import read_sram, pick_crp

sram_data = read_sram('test_sram_data.txt')
address, row = pick_crp(sram_data)
print(address)
print(row)