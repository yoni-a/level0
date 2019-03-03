# strike 1 or 2 → "strike!"
# strike 3 → "out!"
# ball 1 to 3 → "ball!"
# ball 4 → "fourball!"

input_lines = input()

ballCount = 0
strikeCount = 0

for _ in range(int(input_lines)):
    s = input()
    if s == "strike":
        strikeCount += 1
        if strikeCount <= 2:
            print("strike!")
        else:
            print("out!")
            break
    elif s == "ball":
        ballCount += 1
        if ballCount <= 3:
            print("ball!")
        else:
            print("fourball!")
            break
