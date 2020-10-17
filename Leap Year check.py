#start

year = int(input('Enter a year to identify leap year or not:\n'))

if year % 4 == 0:
    print('{} is leap year'.format(year))
else:
    print('{} is not leap year'.format(year))

#end