#problem(b)
# write a function that will print A -Z and a-z with the help of ASCII

def uppercase_alphabet():
    i = 65
    print("\nAll Upper Case Alphabets: ")
    while i <= 90:
        print(chr(i), end=' ')
        i += 1

def lowercase_alphabet():
    i = 97
    print("\n\nAll Lower Case Alphabets: ")
    while i <= 122:
        print(chr(i), end=' ')
        i += 1
    print('\n')

uppercase_alphabet()
lowercase_alphabet()