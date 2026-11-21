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
        