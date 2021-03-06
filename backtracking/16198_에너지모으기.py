import sys

input = sys.stdin.readline

def makeanswer(weights, energy = 0):
    global maxi
    if len(weights) ==3:
        energy += (weights[0] * weights[2])
        if maxi < energy:
            maxi = energy
        return
    else:
        for i in range(1, len(weights)-1): # 고를수 있는 경우의 수
            next = weights[:i] + weights[i+1:]
            makeanswer(next, energy + (weights[i-1] * weights[i+1]))

n = int(input())

weights = list(map(int,input().split()))
maxi = 0
makeanswer(weights)
print(maxi)