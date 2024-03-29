# 이때까지 배웠던 것을 활용해서 Blockchain class 만들기
# 학번 :
# 이름 : 

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
    # mine 변수 선언하여 None 할당 (proof_of_work 결과값 담을 변수) 
    self.mine = None
    # 최초의 블록
    self.new_block(nonce=100, previous_hash=1) # gensis block
  
  # 블록 추가
  def new_block(self, nonce, previous_hash=None):
    # 블록 구조 + current_hash 원소 추가
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'nonce': nonce,
      'previous_hash': previous_hash or self.hash(self.chain[-1]), # self.hash(self.chain[len(self.chain)-1])
      'validation_value': self.mine
    }
    # 현재 트랜잭션 비우기
    self.current_transactions = []
    # mine 변수 ""로 초기화
    self.mine = ""
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
    # prev_block_hash에 prev_block을 hash 함수 취한 값을 할당
    prev_block_hash = hash(prev_block)
    # valid_proof 호출
    while self.valid_proof(prev_block_hash, self.current_transactions, nonce) is False:
      nonce += 1 # 랜덤 값으로 바꾸기
    # new_transactions 호출 -- 채굴 보상 50코인
    self.new_transactions('system', 'me', 50)
    # new_block 호출
    self.new_block(nonce)
    print()

  def valid_proof(self, prev_block_hash, current_transactions, nonce):
     # guess 변수에 prev_block_hash, current_transactions, nonce를 합친 문자열 encode 함수 취하기
    guess = (str(prev_block_hash)+str(current_transactions)+str(nonce)).encode()
    # guess_hash 변수에 guess를 sha256 함수 취한 값을 할당하기
    guess_hash = hashlib.sha256(guess).hexdigest()
    # print() 할 때, 커서 맨 앞으로 위치시켜 출력하기
    print(guess_hash,end='\r')
    # mine에 결과값 할당
    self.mine = guess_hash
    # 조건 0을 4개로 변환하기
    return guess_hash[:4] == "0000"

bc = Blockchain() # 객체 생성 
# print(bc.last_block()) # previous_hash 값 증명을 하기 위해 출력하는 이전(마지막) 블록
bc.new_transactions('john','smith', 50) # john이 smith에게 50코인 전송
bc.new_transactions('jenny','sujan', 100) # jenny가 sujan에게 100코인 전송
# chappie가 simon에게 150코인 전송 코드 추가하기
bc.new_transactions('chappie','simon', 150)
# 현재 체인 상태를 출력하기
print(json.dumps(bc.chain, indent=2))
# 현재 블록에 저장하기 위해 대기 중인 트랜잭션을 json 형태로 출력하는 코드 추가하기
print(json.dumps(bc.current_transactions, indent=2))
# proof_of_work 호출
bc.proof_of_work(bc.hash(bc.last_block()))
# 현재 체인 상태를 출력하기
print(json.dumps(bc.chain, indent=2))

print("################### 트랜잭션 초기화 확인 ###################")
print(bc.current_transactions)
