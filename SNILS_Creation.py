import random


lst = [random.randrange(0, 10) for i in range(9)]

sum_chisel = 0
for i in range(9):
    sum_chisel += lst[i] * (9 - i)

control = 0
if sum_chisel < 100:
    control = sum_chisel
elif sum_chisel > 101:
    control = sum_chisel % 101
    if control == 100 or 101:
        control = '00'

for i in lst:
    print(i, end='')
print(control)
