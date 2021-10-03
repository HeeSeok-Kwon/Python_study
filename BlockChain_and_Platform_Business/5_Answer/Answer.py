# 이때까지 배웠던 것을 활용해서 Blockchain class 만들기

import hashlib
import json
from time import time

class Blockchain(object):
  # 생성자
  def __init__(self):
    # 체인
    self.chain = []
    # 현재 트랜잭션
    self.current_transactions = []
    # 최초의 블록
    self.new_block(nonce=100, previous_hash=1) # gensis block
  
  # 블록 추가
  def new_block(self, nonce, previous_hash=None):
    # 블록 구조
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'nonce': nonce,
      'previous_hash': previous_hash or self.hash(self.chain[-1])
    }
    # 현재 트랜잭션 비우기
    self.current_transactions = []
    # 체인에 블록 연결하기
    self.chain.append(block)

    return block

  # 트랜잭션 추가
  def new_transactions(self, sender, recipient, amount):
    # 현재 트랜잭션에 추가
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })

  def hash(self, block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  def last_block(self):
    # 체인의 마지막 원소 반환
    return self.chain[-1]
  
  # 채굴
  def proof_of_work(self, prev_block):
    # 난스 값 0으로 할당
    nonce = 0
    # valid_proof 호출
    while self.valid_proof(prev_block, nonce) is False:
      nonce += 1
    # new_block 호출
    self.new_block(nonce)
    print()

  def valid_proof(self, prev_block, nonce):
    guess = (str(prev_block)+str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # print() 할 때, 커서 맨 앞으로 위치시켜 출력하기
    print(guess_hash,end='\r')
    # 조건 0이 4개로 변환하기
    return guess_hash[:4] == "0000"

bc = Blockchain() # 객체 생성 
bc.new_transactions('john','smith', 50) # john이 smith에게 50코인 전송
bc.new_transactions('jenny','sujan', 100) # jenny가 sujan에게 100코인 전송
# chappie가 simon에게 150코인 전송 코드 추가하기
bc.new_transactions('chappie','simon', 150)
# 현재 체인 상태를 출력하기
print(json.dumps(bc.current_transactions, indent=2))
# 현재 블록에 저장하기 위해 대기 중인 트랜잭션을 json 형태로 출력하는 코드 추가하기
print(json.dumps(bc.chain, indent=2))
# proof_of_work 호출
bc.proof_of_work(bc.hash(bc.last_block()))
# 현재 체인 상태를 출력하기
print(json.dumps(bc.chain, indent=2))
  
