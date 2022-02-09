# reader function
def reader_func(file_name):
    with open(file_name, 'r') as file:
        print(file.read())

# append function
def append_func(file_name, content):
    with open(file_name,'a') as file:
        line = content
        file.write(line)

