# Slobodeniuk Sasha Andreyevich 23.10.2004
#
# [SN] = Slobodeniuk; [DD]=23; [YYYY] = 2004; hash_end = [MM] = 10
# previous_hash = Slobodeniuk
# Nonce = [DDMM] = 2310
# Nonce - випадковим чином, max_Nonce = [102004]

from blockchain import ssa_Blockchain


ssa_blockchain = ssa_Blockchain()

# New Block №2
ssa_blockchain.ssa_new_transaction(ssa_sender='Sasha', ssa_recipient='Bank', ssa_amount=102004)
ssa_blockchain.ssa_new_transaction(ssa_sender="Bob", ssa_recipient="Charlie", ssa_amount=12312)

ssa_last_block = ssa_blockchain.ssa_last_block
# ssa_proof, ssa_iterations = ssa_blockchain.ssa_proof_of_work(ssa_last_block)
ssa_blockchain.ssa_new_block(ssa_previous_hash=ssa_blockchain.ssa_hash(ssa_last_block))
# print (new_block1, iterations1)

# New Block №3
ssa_blockchain.ssa_new_transaction(ssa_sender='Sasha1', ssa_recipient='Bank1', ssa_amount=10004)
ssa_blockchain.ssa_new_transaction(ssa_sender="Bob1", ssa_recipient="Charlie1", ssa_amount=1212)

ssa_last_block = ssa_blockchain.ssa_last_block

ssa_blockchain.ssa_new_block(ssa_previous_hash=ssa_blockchain.ssa_hash(ssa_last_block))



ssa_blockchain.ssa_print_chain()















