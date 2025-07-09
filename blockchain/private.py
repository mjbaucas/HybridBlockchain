import datetime
from blockchain.block import Block

class Chain:
    def __init__(self):
        self.chain = [gen_genesis_block()]

    def gen_next_block(self, public_key, transactions):
        prev_block = self.chain[-1]
        index = prev_block.index + 1
        timestamp = datetime.datetime.now()
        data = transactions
        hashed_block = prev_block.gen_hashed_block()
        self.chain.append(Block(index, timestamp, data, hashed_block, public_key))
    
    def display_contents(self):
        for block in self.chain:
            block.disp_block_info()
    
    def output_ledger(self):
        main_transactions = []
        for block in self.chain:
            if block.index != 0:
                temp_transactions = block.get_block_transactions()
                for temp_transaction in temp_transactions:
                    main_transactions.append(temp_transaction)
        return main_transactions

    def search_ledger(self, key):
        temp_list = []
        for i in self.chain[::-1]:
            for j in i.transactions:
                temp_list = temp_list + [x for x in i.transactions if x["ID"] == key]
        
        return temp_list.copy()

def gen_genesis_block():
    transaction = [
        {
            "ID": "default", 
            "response": "xxxxxxxx", 
            "sram_address": "0",
            "row_address": 0,
            "timestamp": "0"
        }
    ]
    return Block(0, datetime.datetime.now(), transaction, "0", "0")