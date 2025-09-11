class BankAccount:
    def _init_(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")

    def get_balance(self):
        return self.__balance


class SBI(BankAccount):
    def _init_(self, balance=0):
        super()._init_(balance)  # initialize balance using parent

# Test BankAccount
acc = BankAccount(0)
acc.deposit(5000)
acc.withdraw(2000)
print("Final balance:", acc.get_balance())

# Test SBI account
sbi_acc = SBI(1000)
sbi_acc.deposit(2000)
sbi_acc.withdraw(500)
print("SBI account balance:", sbi_acc.get_balance())