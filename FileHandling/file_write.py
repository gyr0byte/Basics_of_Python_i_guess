filename = "FileHandling/test2.txt"

with open(filename, 'r') as rf:
   with open("FileHandling/test2_copy.txt", "w") as wf:
       for line in rf:
           wf.write(line) 