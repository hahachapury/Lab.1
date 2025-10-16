'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Дмитрий')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

h, w = 20, 30
cx, cy = w // 2, h // 2
r = 6


def circle(x, y):
    return (x - cx)**2 + (y - cy)**2 <= r**2

for y in range(h):
    for x in range(w):
        if circle(x, y):
            print(f"{RED}  {END}", end="")
        else:
            print(f"{WHITE}  {END}", end="")
    print()

print("task2")
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

h, w = 15, 40
R = 7

for y in range(h):
    for x in range(w):
        d1 = abs(x - 10) + abs(y - 7)
        d2 = abs(x - 25) + abs(y - 7)
        if d1 == R or d2 == R:
            print(f"{BLACK}  {END}", end="")
        else:
            print(f"{WHITE}  {END}", end="")
    print()

print('task3')
for y in range(h, -1, -1):
        for x in range(w + 1):
            if x*3== y:
                print(f"{RED} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()

true = sum(float(x)<-5 for x in open('sequence.txt'))
ln=sum(float(x)<=0 for x in open('sequence.txt'))
print(f'{true*100/ln}%[{RED}{' '*true}{END}{WHITE}{' '*(ln-true)}{END}]')