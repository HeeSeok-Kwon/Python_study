current_transactions = []

def new_transactions(sender, recipient, amount):
    current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })

    return current_transactions


new_transactions('john1','smith1', 50)
new_transactions('john2','smith2', 100)
new_transactions('john3','smith3', 150)

print(current_transactions) 

import json
print(json.dumps(current_transactions, indent=2)) # json 형태로 출력
