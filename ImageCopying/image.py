filename = "ImageCopying/cat.png"

with open(filename, 'rb') as rf:
   with open("ImageCopying/cat_copy.png", "wb") as wf:
       for line in rf:
           wf.write(line)