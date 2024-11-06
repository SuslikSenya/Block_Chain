class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Bank:
    def __init__(self, value: int):
        self.value = value
        self.container = []

    def __repr__(self):
        return f'Bank({self.value})'


class Wallet:
    def __init__(self, *banknots: Bank):
        self.container = []
        self.container.extend(banknots)

    def __repr__(self):
        return f'Wallet{self.container}'

    def __iter__(self) -> []:
        return Iterator(self.container)


if __name__ == '__main__':
    fifty = Bank(50)
    hundred = Bank(100)
    five_hundred = Bank(500)
    # print(fifty)
    # print(hundred)
    wallet = Wallet(fifty, hundred, five_hundred)
    for money in wallet:
        print(money)









# # Создание блокчейна и добавление транзакций
# ssa_blockchain = ssa_Blockchain()
#
# # Новый блок №2
# ssa_blockchain.ssa_new_transaction(ssa_sender='Sasha', ssa_recipient='Bank', ssa_amount=102004)
# ssa_blockchain.ssa_new_transaction(ssa_sender="Bob", ssa_recipient="Charlie", ssa_amount=12312)
#
# ssa_last_block = ssa_blockchain.ssa_last_block
# ssa_blockchain.ssa_new_block(ssa_previous_hash=ssa_blockchain.ssa_hash(ssa_last_block))
#
# ssa_blockchain.ssa_new_transaction(ssa_sender='Sasha1', ssa_recipient='Bank1', ssa_amount=10004)
# ssa_blockchain.ssa_new_transaction(ssa_sender="Bob1", ssa_recipient="Charlie1", ssa_amount=1212)
#
# ssa_last_block = ssa_blockchain.ssa_last_block
# ssa_blockchain.ssa_new_block(ssa_previous_hash=ssa_blockchain.ssa_hash(ssa_last_block))
#
# ssa_blockchain.ssa_print_chain()