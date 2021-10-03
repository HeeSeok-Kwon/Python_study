# 이때까지 배웠던 것을 활용해서 Blockchain class 만들기

import hashlib
import json
from time import time

class Blockchain(object):
  # 생성자
  def __init__(self):
    # 체인
    # 현재 트랜잭션
    # mine 변수 선언하여 None 할당 (proof_of_work 결과값 담을 변수) 
    # 최초의 블록
    pass
  
  # 블록 추가
  def new_block(self, nonce, previous_hash=None):
    # 블록 구조 + current_hash 원소 추가
    # 현재 트랜잭션 비우기
    # mine 변수 ""로 초기화
    # 체인에 블록 연결하기

    return block

  # 트랜잭션 추가
  def new_transactions(self, sender, recipient, amount):
    # 현재 트랜잭션에 추가
    pass

  def hash(self, block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  def last_block(self):
    # 체인의 마지막 원소 반환
    pass
  
  # 채굴
  def proof_of_work(self, prev_block):
    # 난스 값 0으로 할당
    # valid_proof 호출
    # new_block 호출
    print() # 채굴 후에 출력창 구분하기 위해 추가한 코드
    

  def valid_proof(self, prev_block, nonce):
    # print() 할 때, 커서 맨 앞으로 위치시켜 출력하기
    # mine에 결과값 할당
    # 조건 0이 4개로 변환하기
    pass


bc = Blockchain() # 객체 생성 
bc.new_transactions('john','smith', 50) # john이 smith에게 50코인 전송
bc.new_transactions('jenny','sujan', 100) # jenny가 sujan에게 100코인 전송
# chappie가 simon에게 150코인 전송 코드 추가하기

# 현재 체인 상태를 출력하기

# 현재 블록에 저장하기 위해 대기 중인 트랜잭션을 json 형태로 출력하는 코드 추가하기

# proof_of_work 호출

# 현재 체인 상태를 출력하기


  
