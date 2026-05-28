class BankAccount:
  def __init__ (self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin 
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance +=amount
    else: 
      print("Invalid nummber")
  
  def withdraw(self, amount):
    if self.balance > 0:
      self.balance -=amount
    else: 
      print("Invalid nummber")

  def display_balance(self):
    print(self.balance)

singh  = BankAccount("Hartej", "Singh", 1, "Savings", 1234, 0.00) 


singh.withdraw(25)
singh.display_balance()