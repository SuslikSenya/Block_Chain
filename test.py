import json
import hashlib
from dataclasses import dataclass, asdict
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

SN = 'Slobodeniuk'
NONCE = 2310
YYYY = 2004
DD = 23
MMYYYY = 102004
MM = "10"


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: float = None

    def __post_init__(self):
        self.timestamp = time()


@dataclass
class Block:
    index: int
    transactions: list[Transaction]
    previous_hash: str
    proof: int
    timestamp: float = None

    def __post_init__(self):
        self.timestamp = time()


class ssa_Blockchain(object):
    def __init__(self) -> None:
        self.ssa_chain = []
        self.ssa_current_transactions = []
        self.current_nonce = NONCE
        self.reward = YYYY
        self.node_identifier = str(uuid4()).replace('-', '')

        self.ssa_new_transaction(ssa_sender='0', ssa_recipient=self.node_identifier, ssa_amount=0)
        self.ssa_new_block(previous_hash=SN)

    def ssa_new_block(self, previous_hash=None):
        block = Block(index=len(self.ssa_chain) + 1,
                      transactions=self.ssa_current_transactions[:],
                      previous_hash=previous_hash or self.ssa_hash(self.ssa_chain[-1]),
                      proof=self.current_nonce)

        self.ssa_current_transactions = []
        block.proof, block.iterations = self.ssa_proof_of_work(block)
        self.ssa_chain.append(block)

        # print(self.reward)
        if block.index % 2 == 0:
            self.reward /= (int(MM) + 1)
        return block

    def ssa_new_transaction(self, ssa_sender, ssa_recipient, ssa_amount):
        transaction = Transaction(ssa_sender, ssa_recipient, ssa_amount)
        self.ssa_current_transactions.append(transaction)

        return len(self.ssa_chain) + 1 if self.ssa_chain else 1

    @staticmethod
    def ssa_hash(ssa_block):
        ssa_block_string = json.dumps(asdict(ssa_block), sort_keys=True).encode()
        return hashlib.sha256(ssa_block_string).hexdigest()

    @property
    def ssa_last_block(self):
        return self.ssa_chain[-1]

    def ssa_proof_of_work(self, ssa_block):
        ssa_iterations = 0
        ssa_proof = self.current_nonce

        while True:
            if self.ssa_valid_proof(ssa_block, ssa_proof) and ssa_proof <= MMYYYY:
                self.current_nonce = ssa_proof
                break
            ssa_proof += 1
            ssa_iterations += 1

        return ssa_proof, ssa_iterations

    def ssa_valid_proof(self, ssa_block, ssa_proof):
        ssa_block.proof = ssa_proof
        ssa_guess_hash = self.ssa_hash(ssa_block)

        return ssa_guess_hash[-2:] == MM

    def ssa_print_chain(self):
        for ssa_block in self.ssa_chain:
            print(f"Block {ssa_block.index}:")
            print(f"  Previous Hash: {ssa_block.previous_hash}")
            print(f"  Current Hash: {self.ssa_hash(ssa_block)}")
            print(f"  Nonce: {ssa_block.proof}")
            print(f"  Iterations per proof: {self.ssa_proof_of_work(ssa_block)[1]}")
            print(f"  Transactions: {ssa_block.transactions}")
            print(f"  Timestamp: {ssa_block.timestamp}")
            print()


# Створюємо екземпляр вузла
app = Flask(__name__)

# Генеруємо унікальну на глобальному рівні адресу для цього вузла
node_identifier = str(uuid4()).replace('-', '')

# Створюємо екземпляр блокчейну
blockchain = ssa_Blockchain()


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Blockchain API!"


# Створення кінцевої точки /mine, яка є GET-запитом
@app.route('/mine', methods=['GET'])
def mine():
    # Запускаємо алгоритм підтвердження роботи, щоб отримати наступний пруф
    last_block = blockchain.ssa_last_block

    blockchain.ssa_new_transaction(ssa_sender="0", ssa_recipient=blockchain.node_identifier, ssa_amount=blockchain.reward)
    previous_hash = blockchain.ssa_hash(last_block)
    new_block = blockchain.ssa_new_block(previous_hash=previous_hash)

    response = {
        'message': "New Block was Made",
        'index': new_block.index,
        'transactions': new_block.transactions,
        'proof': new_block.proof,
        'previous_hash': new_block.previous_hash,
    }
    return jsonify(response), 200


# Створення кінцевої точки /transactions/new, яка є POST-запитом, так як будемо відправляти туди дані;
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Перевірка того, що необхідні поля знаходяться серед POST-даних
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Створення нової транзакц
    index = blockchain.ssa_new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


# Створення кінцевої точки /chain, яка повертає весь блокчейн;
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.ssa_chain,
        'length': len(blockchain.ssa_chain),
    }
    return jsonify(response), 200


def main():
    blockchain = ssa_Blockchain()

    # Майнимо ((DD+1) mod 13) блоків
    num_blocks_to_mine = (DD + 1) % 13
    print(f"Кількість блоків котрі треба намайнити = ((DD+1) mod 13) = {num_blocks_to_mine}")
    reward = 0
    for _ in range(num_blocks_to_mine - 1):
        blockchain.ssa_new_transaction("Sasha", "Bank", 2004)
        blockchain.ssa_new_block(previous_hash=blockchain.ssa_hash(blockchain.ssa_last_block))
        reward += blockchain.reward
        print(blockchain.ssa_last_block)
    blockchain.ssa_print_chain()
    print(reward)


# Запускає сервер на порт: 5000

if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=5000)
