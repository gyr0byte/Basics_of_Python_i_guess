filename = 'ExceptionHandling/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)

# with will automatically close the file at the end, no need to use finally block/ file.close()
