# 재귀함수
# - 내가 나를 호출
# - 반복문 <-> 재귀함수

# def solution():
#     sum = 0
#     n=100
#     # sum = 1 곱
#     for i in range(1, n+1):
#         sum += i
#         # sum *= i 곱
#     print(sum)
# O(n)

# 시그마 공식: n*(n+1)//2
def solution():
    sum = 0
    n = 100
    sum = n*(n+1)//2
    print(sum)
# O(1)


solution()
