'''
1. 리스트에서 원소를 차례대로 비교
2. 비교할 때 두 원소를 기준으로 오름차순 / 내림차순 여부를 체크

input

1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
8 1 7 2 6 3 5 4

output  

ascending
descending
mixed

'''

a = list(map(int , input().split()))

ascending = True
descending = True

for i in range(1, 8):
    if a[i-1] < a[i]:
        descending = False
    elif a[i-1] > a[i]:
        ascending = False
    
if ascending == descending:
    print("mixed")
elif ascending == False:
    print("descending")
elif descending == False:
    print("ascending")