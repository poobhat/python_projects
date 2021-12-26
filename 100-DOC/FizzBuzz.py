s = ''
for i in range(1, 100):
    if i%3 == 0: s+='fizz'
    if i%5 == 0: s+='buzz'

    print(s if s else i)