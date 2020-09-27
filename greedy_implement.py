# Greedy
# - 현재 상황에서 당장 좋은 것만 고르는 방법
# - 정당성 분석이 중요

# 문제. 거스름 돈 : 문제 해결 아이디어
# - 가장 큰 화폐단위부터 계산

n = 1260
count = 0
remain = n

array = [500,100,50,10]

for coin in array:
    count += n // coin
    n %= coin
print(count)

# 문제. 1이 될 때까지
# 주어진 N에 대하여 최대한 많이 나누기
# N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 줄일 수 있음

n, k = map(int, input().split())

result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result +=1
    n //= k

result += (n-1)
print(result)

# 문제. 곱하기 혹은 더하기
# 대부분의 경우 + 보다는 x가 값을 더 크게 만듦

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <=1:
        result += num
    else
        result *= num

print(result)

