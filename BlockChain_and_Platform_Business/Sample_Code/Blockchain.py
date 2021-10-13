# https://blog.naver.com/pjt3591oo/221181592127

import hashlib
import json
from time import time

class Blockchain(object): 
  # 생성자
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.mine = None
    self.new_block(nonce=100, previous_hash=1) # gensis block
  
  # 블록 추가
  def new_block(self, nonce, previous_hash=None):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'nonce': nonce,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
      'current_hash': self.mine
    }

    self.current_transactions = [] # 버퍼 비우기
    self.mine = ""
    self.chain.append(block)

    return block

  # 트랜잭션 추가
  def new_transactions(self, sender, recipient, amount):

    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })

    # return self.last_block['index']+1

  def hash(self, block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  def last_block(self):
    return self.chain[-1]
  
  # 채굴
  def proof_of_work(self, prev_block):
    nonce = 0
    while self.valid_proof(prev_block, nonce) is False:
      nonce += 1
    self.new_block(nonce)
    print()
    # return nonce

  def valid_proof(self, prev_block, nonce):
    # guess = str(prev_nonce*nonce).encode()
    guess = (str(prev_block)+str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash,end='\r')
    self.mine = guess_hash
    return guess_hash[:4] == "0000"

bc = Blockchain()
bc.new_transactions('john1','simon1', 50)
bc.new_transactions('john2','simon2', 50)
print(json.dumps(bc.current_transactions, indent=2))
print(json.dumps(bc.chain, indent=2))
# bc.proof_of_work(bc.last_block()['nonce'])
bc.proof_of_work(bc.hash(bc.last_block()))
print(json.dumps(bc.chain, indent=2)) 
