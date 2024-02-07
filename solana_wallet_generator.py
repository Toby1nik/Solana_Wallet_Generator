import os
from solders.keypair import Keypair


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def account_generator():
    """Return address and privateKey in base58"""
    account = Keypair()
    address = account.pubkey()
    priv_key = account.from_json(account.to_json())

    return address, priv_key


if __name__ == '__main__':
    name_file = str(input("Name file with keys (without txt): "))
    amount = int(input("How much accounts create: "))
    show_key = str(input("Printed private key and address (y/n): "))
    i = 0

    directory = "SolPrivKeys"
    create_directory_if_not_exists(directory)

    while i != amount:
        address, private_key = account_generator()
        if show_key.lower() == 'y':
            print(f"Private Key: {private_key} | Address: {address}")
        with open(file=os.path.join(directory, f"{name_file}.txt"), mode='a', encoding='utf-8-sig') as file:
            file.write(f'{private_key}\n')
        i += 1





