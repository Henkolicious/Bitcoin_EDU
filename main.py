# Namn:                 Henrik Larsson
# E-post:               me@henriklarsson.eu
# python --version:     3.6.5

import sys
import platform
import requests
import json
from datetime import datetime

# settings
rpc_user = 'alice'
rpc_pass = 'bob'
url = 'http://%s:%s@localhost:8332' % (rpc_user, rpc_pass)
headers = {'content-type': 'application/json'}


class Transaction():
    def __init__(self, block, txid, amout):
        self.block = block
        self.txid = txid
        self.amout = str(amout) + " BTE"


def get_chain_info():
    payload = {
        "method": "getblockchaininfo"
    }
    resp = requests.post(url, data=json.dumps(payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get chain info -->", resp['error'])
        return None


def get_network_info():
    payload = {
        "method": "getnetworkinfo"
    }
    resp = requests.post(url, data=json.dumps(
        payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get network info -->", resp['error'])
        return None


def get_mempool_info():
    payload = {
        "method": "getmempoolinfo"
    }
    resp = requests.post(url, data=json.dumps(
        payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get mempool info -->", resp['error'])
        return None


def get_block_hash(block_number: int):
    payload = {
        "method": "getblockhash",
        "params": [block_number]
    }
    resp = requests.post(url, data=json.dumps(
        payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get block hash -->", resp['error'])
        return None


def get_block(block_hash: str):
    payload = {
        "method": "getblock",
        "params": [block_hash, True]
    }
    resp = requests.post(url, data=json.dumps(
        payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get block -->", resp['error'])
        return None


def get_raw_transaction(TXID):
    payload = {
        "method": "getrawtransaction",
        "params": [TXID, True]
    }

    resp = requests.post(url, data=json.dumps(
        payload), headers=headers).json()

    if (resp['error'] == None):
        return resp['result']
    else:
        print("## Error: could not get transaction -->", resp['error'])
        return None


def print_transactions(txs):
    print("Transaktioner:")
    for it in enumerate(txs):
        print(" ", it[0], ":", it[1])


def get_max_block_nr() -> int:
    chain_resp = get_chain_info()
    return int(chain_resp['blocks'])


def get_transactions(txs):
    result_csv = ""
    for tx in txs:
        result_csv = result_csv + tx + ","
    return result_csv[:-1]


def get_transaction_list(target_adress):
    result = []
    print("Hittade inget bra RPC anrop att använda, så handjagar detta på klientsidan, \nvilket är idiotiskt då det blir en jävla massa anrop.")
    print("CTRL + C, för att avbryta.\n--------")
    totalCount = get_max_block_nr()
    for idx in range(totalCount):
        if idx == 0:
            # ignore root
            continue

        print("Söker på index:", str(idx) + "/" + str(totalCount))
        block_hash = get_block_hash(idx)
        block = get_block(block_hash)
        transactions = get_transactions(block['tx'])

        for trans in transactions.split(','):
            tran = get_raw_transaction(trans)

            for it in enumerate(tran['vout']):
                for addr in get_addresses(it[1]['scriptPubKey']).split(','):
                    if (addr == target_adress):
                        tmp = Transaction(
                            block['height'], block['tx'], it[1]['value'])
                        result.append(tmp)
    return result


def show_block_by_number():
    block_number = input("Ange block-nummer: ")
    block_hash = get_block_hash(int(block_number))
    block = get_block(block_hash)
    print("----------------------------------------------------------------------------------------------------")
    print("Block hash:            ", block['hash'])
    print("Föregående hash:       ", block['previousblockhash'])
    print("Merkle root:           ", block['merkleroot'])
    print("Höjd:                  ", block['height'])
    print("Tid:                   ", datetime.utcfromtimestamp(
        block['time']).strftime('%Y-%m-%d %H:%M:%S'))
    print("Svårighet:             ", block['difficulty'])
    print("Antal transaktioner:   ", block['nTx'])
    print_transactions(block['tx'])
    print("----------------------------------------------------------------------------------------------------")


def show_block_by_hash():
    block_hash = input("Ange transaktionshash: ")
    block = get_block(block_hash)
    print("----------------------------------------------------------------------------------------------------")
    print("Block hash:            ", block['hash'])
    print("Föregående hash:       ", block['previousblockhash'])
    print("Merkle root:           ", block['merkleroot'])
    print("Höjd:                  ", block['height'])
    print("Tid:                   ", datetime.utcfromtimestamp(
        block['time']).strftime('%Y-%m-%d %H:%M:%S'))
    print("Svårighet:             ", block['difficulty'])
    print("Antal transaktioner:   ", block['nTx'])
    print_transactions(block['tx'])
    print("----------------------------------------------------------------------------------------------------")


def show_block_trasaction():
    transaction_id = input("Ange transaktionshash: ")
    transaction = get_raw_transaction(transaction_id)
    print("----------------------------------------------------------------------------------------------------")
    print("Txid (hash):            ", transaction['txid'])
    print("Tillhör block:          ", transaction['blockhash'])
    print("Inputs:                 ", len(transaction['vin']))
    print_transaction_outputs(transaction['vout'])
    print("----------------------------------------------------------------------------------------------------")


def show_outputs_for_adress():
    adress = input("Ange adress: ")
    transaction_list = get_transaction_list(adress)
    print("Transaktioner:\n----------")
    for tran in transaction_list:
        print(" Storlek: ", tran.amout)
        print(" Block:   ", tran.block)
        print(" ID:      ", tran.txid[0])
        print()


def print_chain_info():
    chain_resp = get_chain_info()
    network_resp = get_network_info()
    mempool_resp = get_mempool_info()
    print("====================================================================================================")
    print("Antal block:                  ", chain_resp['blocks'])
    print("Lagringsstorlek:              ", chain_resp['size_on_disk'])
    print("Högsta validerade best-block: ", chain_resp['bestblockhash'])
    print("Mempool (size):               ",
          mempool_resp['size'], "st transaktioner")
    print("Anslutningar:                 ",
          network_resp['connections'], "noder")
    print("====================================================================================================")


def get_addresses(scriptPubKey) -> str:
    try:
        result = ""
        for addr in enumerate(scriptPubKey['addresses']):
            result = result + addr[1] + ","
        return result[:-1]
    except:
        return "adress saknas"


def print_transaction_outputs(vout):
    print("Outputs:                 ", len(vout))
    counter = 1
    for it in enumerate(vout):
        print(counter, ":", it[1]['value'], "BTE till",
              get_addresses(it[1]['scriptPubKey']))
        counter = counter + 1


def user_choice(user_input):
    if (user_input == "0"):
        print("\nAvslutar programmet...\n")
        sys.exit()
    try:
        if (user_input == "1"):
            show_block_by_number()

        elif (user_input == "2"):
            show_block_by_hash()

        elif (user_input == "3"):
            show_block_trasaction()

        elif (user_input == "4"):
            show_outputs_for_adress()

        elif (user_input == "5"):
            print_chain_info()

        else:
            print("##### Ogiltigt val, försök igen. #####")

    except:
        print("##### Nu gick något galet och ingen felhantering är implementerad heller. Taffligt värre. #####")


if __name__ == "__main__":
    print_chain_info()
    print()

    while (True):
        print("Meny")
        print(" 1. Visa block (ange nr)")
        print(" 2. Visa block (ange hash)")
        print(" 3. Visa transaktion")
        print(" 4. Lista outputs för adress")
        print()
        print(" 5. Visa startinfo")
        print(" 0. Avsluta")
        print()
        user_input = input("Välj funktion: ")
        user_choice(user_input)
        print()
