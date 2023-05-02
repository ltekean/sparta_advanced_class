# 재귀함수 (코딩테스트)
# 재귀함수 : 스스로 정의하는 함수
# bfs
# dfs
# 정렬 알고리즘

def recursional(n):
    if n >=5:
        print(n)
        recursion(n+1)

recursional(1) # 1 2 3 4

def recursion(n):
    if n <=0:
        return 0
    return n + recursion(n-1)

print(recursion(4)) # 10

# 팩토리얼 계산법
def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a-1)
print(factorial(16))

# 피보나치 수열
def fib(b):
    if b == 1:
        return 0
    elif b == 2:
        return 1
    else:
        return fib(b - 1) + fib(b - 2)
    


# class 심화 (장고 공부)

# method overriding
class Animal:
    def __init__(self) -> None:
        pass
    def speak(self):
        print("동물 소리")
        
class dog(Animal):
    def speak(self):
        print("개소리")

class cat(Animal):
    def speak(self):
        print("야옹")

Dog = dog("강아지")
Cat = cat("고냥이")


# 모델 클래스 오버라이딩

# 추상 클래스
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def tear(self):
        pass
