input_lines = input()

xten = False
zero = False
maxNum = 0
total = 0

s = input().split(' ')
for i in range(int(input_lines)):
    if s[i].startswith('x'):
        xten = True
    else:
        temp = int(s[i])
        if temp > maxNum:
            maxNum = temp
        if int(temp) == 0:
            zero = True
        else:
            total += temp

if zero:
    total -= maxNum
if xten:
    total = total * 10

print(total)