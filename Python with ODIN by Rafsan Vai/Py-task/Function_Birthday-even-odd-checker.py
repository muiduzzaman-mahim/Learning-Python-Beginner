def birthday_checker(date):
    if date%2 == 0:
        print('{} is Even Number.'.format(date))
    else:
        print('{} is Odd Number.'.format(date))

date = int(input('Enter your date of birth or year of birth: \n'))
birthday_checker(date)