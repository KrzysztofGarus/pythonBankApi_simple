from flask import Flask, request, jsonify
from BankAccount import BankAccount

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def create_account():
    number = int(request.args.get('number', 0))
    balance = float(request.args.get('balance', 0))
    account = BankAccount(number, balance)
    BankAccount.bank_accounts[number] = account
    return f'Created account number {number} with balance: {balance} PLN'


@app.route('/accounts', methods=['GET'])
def show_accounts():
    account_info = [f'Account number: {account.number}, Balance: {account.balance} PLN' for number, account in BankAccount.bank_accounts.items()]
    return '\n'.join(account_info)


@app.route('/balance', methods=['GET'])
def show_balance():
    number = int(request.args.get('number', 0))
    if number in BankAccount.bank_accounts:
        account = BankAccount.bank_accounts[number]
        return f'Balance of account {number} is {account.get_balance()}'
    else:
        return f'Account with number {number} does not exist'


@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.args.get('amount', 0))
    number = int(request.args.get('number', 0))
    if number in BankAccount.bank_accounts:
        account = BankAccount.bank_accounts[number]
        return account.deposit(amount)
    else:
        return 'Account number does not exist'


@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.args.get('amount', 0))
    number = int(request.args.get('number', 0))
    if number in BankAccount.bank_accounts:
        account = BankAccount.bank_accounts[number]
        return account.withdraw(amount)
        return
    else:
        return 'Account number does not exist'


@app.route('/transfer', methods=['POST'])
def transfer():
    amount = float(request.args.get('amount', 0))
    number_from = int(request.args.get('number_from', 0))
    number_to = int(request.args.get('number_to', 0))
    if number_from and number_to in BankAccount.bank_accounts:
        account_to = BankAccount.bank_accounts[number_to]
        account_from = BankAccount.bank_accounts[number_from]
        return account_from.transfer(account_to, amount)
    else:
        return 'Account number does not exist'


if __name__ == '__main__':
    app.run(debug=True)
