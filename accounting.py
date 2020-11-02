from user.authentication import authenticate_user
from transactions.journal import *
import banking
import sys

f __name__ == "__main__":
    if len(sys.argv) > 1:
        count = 1
        for i in range(len(sys.argv) - 1):
            print(sys.argv[count])
            count += 1
    authenticate_user()
    receive_income(100)
    pay_expense(100)
    banking.reconciliation.do_reconciliation()