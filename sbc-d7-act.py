import random

def print_menu():
  print("1. Create an Account")
  print("2. Check Account Balance")
  print("3. Withdraw Money")
  print("4. Deposit Money")
  print("5. Exit")
  print()

accounts = {}
balances = {}

def get_account_number():
  while True:
    try:
      account_number = int(input("Enter your account number: "))
      return account_number
    except ValueError:
      print("Please enter a valid account number (digits only).")

def check_balance(account_number):
  if account_number in accounts:
    print(f"Account number: {account_number}, Balance: ₱{balances[account_number]}")
  else:
    print("Account number not found.")

def create_account():
  max_attempts = 10
  for _ in range(max_attempts):
    account_number = random.randint(10000, 99999)
    if account_number not in accounts:
      accounts[account_number] = True
      initial_balance = float(input("Enter initial balance: "))
      balances[account_number] = initial_balance
      print(f"Account number {account_number} created!")
      return
  print("Unable to create a new account. Please try again.")

def withdraw(account_number):
  if account_number in accounts:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount <= balances[account_number]:
      balances[account_number] -= withdraw_amount
      print(f"Your new balance is ₱{balances[account_number]}")
    else:
      print("Insufficient funds.")
  else:
    print("Account number not found.")

def deposit(account_number):
  if account_number in accounts:
    deposit_amount = float(input("Enter amount to deposit: "))
    balances[account_number] += deposit_amount
    print(f"Your new balance is ₱{balances[account_number]}")
  else:
    print("Account number not found.")

print_menu()

while True:
  try:
    choice = int(input("Select an option (1-5): "))
    if choice == 1:
      create_account()
    elif choice == 2:
      check_balance(get_account_number())
    elif choice == 3:
      withdraw(get_account_number())
    elif choice == 4:
      deposit(get_account_number())
    elif choice == 5:
      break
    else:
      print("Invalid option. Please choose a number between 1 and 5.")
  except ValueError:
    print("Please enter a valid number.")

  print()
