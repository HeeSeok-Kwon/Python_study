import hashlib
import json
from time import time

i = 0
chain = []
current_transactions = []

def new_transactions(sender, recipient, amount):
    current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })

    return current_transactions

def new_block(nonce, current_transactions=None, previous_hash=None):
    block = {
      'index': i + 1,
      'timestamp': time(),
      'transactions': current_transactions,
      'nonce': nonce,
      'previous_hash': previous_hash or hash(chain[-1])
    }

    chain.append(block)
    current_transactions = []

    return block

def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest() # 16진수 숫자만 포함하는 두 배 길이의 문자열 객체로 반환

def last_block(chain):
  return chain[-1]

def proof_of_work(prev_block):
    nonce = 0
    while valid_proof(prev_block, nonce) is False:
      nonce += 1

    new_block(nonce=nonce, current_transactions=current_transactions)
    print()
    # return nonce

def valid_proof(prev_block, nonce):
    # guess = str(prev_nonce*nonce).encode()
    guess = (str(prev_block)+str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[:3] == "000"


new_block(nonce=100, previous_hash=1) # gensis block
print(chain)
print(json.dumps(chain, indent=2))

new_transactions('john1','smith1', 50)
new_transactions('john2','smith2', 100)
new_transactions('john3','smith3', 150)

proof_of_work(last_block(chain))
print(json.dumps(chain, indent=2))