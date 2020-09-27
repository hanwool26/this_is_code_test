a = [3,5,4,2,1]
print(a)

# slicing
a = [1,2,3,4,5,6,7]
print(a[1:3])

# List comprehension
array = [i for i in range(10) if i % 2 == 0]
print(array)

# 2차원 리스트 초기화
n = 4
m = 3

array = [[0] * m for _ in range(n)] # 내부적으로 parameter를 쓰지 않을 때 _ 를 씀
print(array)

# 자주쓰는 method
# append() / sort() / reverse() / insert() / count() / remove()

# sort와 sorted의 차이점은 sorted() 는 객체를 복사하여 기존값을 변형시키지않음.

# 문자열 자료형
# 문자열 변수를 초기화할 떄는 "", '' 를 사용

# Turple
# - 한번 선언된 값을 변경할 수 없다
# - ()로 구성

a = (1,2,3,4)
print(a)
#a[2] =7 # error because a is turple

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
print(data.keys())
print(data.values())

# 집합 자료형
# - 중복을 허용하지 않음
# - 순서가 없음

data = set([1,1,2,3,4,4,5])
print(data)
a = [1,2,3]
a.append(4)
print(a)

# input method
n = list(map(int, input().split()))
print(n)

n = int(input())
m = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 조건문
x = 16
if x > 15:
    print("x is larger than 15")
else:
    print("x is less than 15")

a = 7
if 0 <= a and a <= 10:
    print('a는 0이상 10 이하')
else:
    pass # 나중에 작성할 코드

score = 85
result = "합격" if score >= 80 else "불합격"

i = 1
result = 0
while i<=9:
    result+=i
    i += 1
print(result)

for i in range(1,10):
    result += i
print(result)

# function
# def 함수명(parameter)
#   ....
#   return

def add(a, b):
    return a+b

print(add(3,7))
print(lambda a,b: a+b,3,7)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

from itertools import product

data = ['a','b','c']
result = list(product(data, repeat=2))
print(result)

from itertools import permutations
result = list(permutations(data,3))
print(result)

