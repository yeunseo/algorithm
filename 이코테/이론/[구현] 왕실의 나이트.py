answer = 0
locate = input()
x = ord(list(locate)[0])
y = int(list(locate)[1])

all_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

for m in all_moves:
    if(ord('a') <= x + m[0] <= ord('h') and 0 < y + m[1] <= 8):
        answer += 1
    
print(answer)

'''
Review
ord() : 문자열 -> 숫자
chr() : 숫자 -> 문자열
'''