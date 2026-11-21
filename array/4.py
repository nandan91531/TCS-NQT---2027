
"""
QUESTION: Bank Transaction Fraud Detection

You are given N bank transactions.

Each transaction contains:
    Sender
    Receiver
    Amount
    Timestamp

A transaction is considered FRAUD if:

1. Sender, Receiver, and Amount are the same.
2. Timestamp difference between two transactions
   is less than or equal to 60 seconds.

Your task is to find and print all such fraud transactions.

-------------------------
EXAMPLE INPUT:
-------------------------
5
ANU JON 200.50 1000
ANU JON 200.50 1050
RAM SAM 300.00 2000
ANU JON 200.50 2000
RAM SAM 300.00 2040

-------------------------
EXPECTED OUTPUT:
-------------------------
Fraud Transactions:
ANU JON 200.5 1000
ANU JON 200.5 1050
RAM SAM 300.0 2000
RAM SAM 300.0 2040

-------------------------
CONSTRAINT:
-------------------------
Timestamp difference <= 60 seconds.

-------------------------
APPROACH:
-------------------------
Use Nested Loops (Brute Force).

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

transactions = []
N = int(input("enter no. of transaction:"))
for i in range(N):
    sender,receiver,amount,timestamp = input().split()  # .split() by default space se split karega
    amount = float(amount)
    timestamp = int(timestamp)
    
    transactions.append([sender,receiver,amount,timestamp])


fraud = set()
for i in range(N-1):
    for j in range(1,N):
        if transactions[i][0]==transactions[j][0] and transactions[i][1]==transactions[j][1] and transactions[i][2]==transactions[j][2] and abs(transactions[i][3] - transactions[j][3]) <=60:
            fraud.add(i)
            fraud.add(j)
            
if fraud:
    for i in range(N):
        if i in fraud:
            print(*transactions[i])
        
else:
    print("no fraud transcation")
        