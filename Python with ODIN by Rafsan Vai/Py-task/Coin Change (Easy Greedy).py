#start program
print('Enter the amount of money to exchange')

money = int(input())

if money >= 1000:
    times = money // 1000 # 2 --> (2200 / 1000)
    
    print('1000 taka note {}.'.format(times))

money = money % 1000
384729
if money >= 500:
    times = money // 500
    print('500 taka note {}.'.format(times))

money = money % 500
if money >= 200:
    times = money // 200
    print('200 taka note {}.'.format(times))

money = money % 200
if money >= 100:
    times = money // 100
    print('100 taka note {}.'.format(times))

money = money % 100
if money >= 50:
    times = money // 50
    # money = money % 50
    print('50 taka note {}.'.format(times))

money = money % 50
if money >= 20:
    times = money // 20
    # money = money % 20
    print('20 taka note {}.'.format(times))

money = money % 20
if money >= 10:
    times = money // 10
    # money = money % 10
    print('10 taka note {}.'.format(times))

money = money % 10
if money >= 5:
    times = money // 5
    # money = money % 5
    print('5 taka note {}.'.format(times))

money = money % 5
if money >= 2:
    times = money // 2
    # money = money % 2
    print('2 taka note {}.'.format(times))

money = money % 2
if money >= 1:
    times = money // 1
    money = money % 1
    print('1 taka note {}.'.format(times))

#end Program