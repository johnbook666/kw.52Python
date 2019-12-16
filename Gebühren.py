print("--- Gebühren Programm ---")
bank_balance = 500
fee = 20
start_year = 2019

for x in range(5):
    bank_balance = bank_balance - fee
    print(str(start_year + x + 1) + ' neuer Kontostand: ' + str(bank_balance))