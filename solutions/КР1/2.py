a = input()
op = input()
b = input()

if len(op) % 2 == 0 and ' ' in op:
    op = '+'
elif len(op) % 2 == 0 and ' ' not in op:
    op = '-'
elif len(op) % 2 != 0 and ' ' in op:
    op = '*'
else:
    op = '//'

print(eval(f'{a}{op}{b}'))
