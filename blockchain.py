import json
import hashlib
from time import time
import random


class ssa_Blockchain(object):
    def __init__(self) -> None:
        self.ssa_chain = []
        self.ssa_current_transactions = []
        self.ssa_new_block(ssa_proof=100, ssa_previous_hash='Slobodeniuk')


    def ssa_new_block(self, ssa_proof=None, ssa_previous_hash=None, ssa_iterations=None):
        ssa_block = {
            'index': len(self.ssa_chain) + 1,
            'timestamp': time(),
            'transactions': self.ssa_current_transactions,
            'proof': ssa_proof,
            'previous_hash': ssa_previous_hash or self.ssa_hash(self.ssa_chain[-1]),
            'iterations': ssa_iterations
        }

        ssa_proof, ssa_iterations = self.ssa_proof_of_work(ssa_block)
        # print(ssa_proof, ssa_iterations)
        # ssa_block['iterations'] = ssa_iterations
        ssa_block['proof'] = ssa_proof

        self.ssa_current_transactions = []
        self.ssa_chain.append(ssa_block)

        return ssa_block
    def ssa_new_transaction(self, ssa_sender, ssa_recipient, ssa_amount):
        self.ssa_current_transactions.append({
            'sender': ssa_sender,
            'recipient': ssa_recipient,
            'amount': ssa_amount
        })

        return self.ssa_last_block['index'] + 1

    @staticmethod
    def ssa_hash(ssa_block):
        ssa_block_string = json.dumps(ssa_block, sort_keys=True).encode()
        return hashlib.sha256(ssa_block_string).hexdigest()

    @property
    def ssa_last_block(self):
        return self.ssa_chain[-1]

    def ssa_proof_of_work(self, ssa_block):
        ssa_iterations = 0

        while True:
            ssa_nonce = random.randint(2310, 102004)
            ssa_iterations += 1
            if self.ssa_valid_proof(ssa_block, ssa_nonce):
                break
        return ssa_nonce, ssa_iterations

    # @staticmethod
    def ssa_valid_proof(self, ssa_block, ssa_nonce):
        ssa_block['proof'] = ssa_nonce
        ssa_guess_hash = self.ssa_hash(ssa_block)

        return ssa_guess_hash[-2:] == "10"

    def ssa_print_chain(self):
        for ssa_block in self.ssa_chain:
            print(f"Block {ssa_block['index']}:")
            print(f"  Previous Hash: {ssa_block['previous_hash']}")
            print(f"  Current Hash: {self.ssa_hash(ssa_block)}")
            print(f"  Proof: {ssa_block['proof']}")
            print(f"  Iterations per proof: {self.ssa_proof_of_work(ssa_block)[1]}")
            print(f"  Transactions: {ssa_block['transactions']}")
            print(f"  Timestamp: {ssa_block['timestamp']}")
            print()
