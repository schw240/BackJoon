
'''
N 장의 카드 , 숫자 M
N장의 카드중 3개를 골라서 합이 M에 가까운 숫자 만들기
input

5 21 카드의 갯수 
5 6 7 8 9 카드에 쓰여진 수

10 500
93 181 245 214 315 36 185 138 216 295

output

21
497

'''

N, M = list(map(int, input().split()))
a = list(map(int, input().split()))

max = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if a[i] + a[j] + a[k] > max and a[i] + a[j] + a[k] <= M:
                max = a[i] + a[j] + a[k]

print(max)
                