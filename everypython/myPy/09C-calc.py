import random

a = random.randint(1,30) # 1~30 사이의 임의의 수를 a에 저장
b = random.randint(1,30)

print(a, "+", b, "=")
x = input() # 답을 입력받아서 x에 저장 (문자열로 저장)
c = int(x) # 문자열을 정수로 변환

if a + b == c:
    print("천재")

else:
    print("바보?")

    
