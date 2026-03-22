filename = "FileHandling/test.txt"

with open(filename, 'r') as f:
    # content = f.read() # Reads the entire file at once
    # content = f.readline() # Reads the file line by line
    # print(content, end = "")
    # content = f.readline()
    # print(content)
    # for line in f:
    #     print(line, end = "") # this is efficient and memory usuage is low
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end = "")
        f_contents = f.read(size_to_read)