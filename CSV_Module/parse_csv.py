import csv
path = "CSV_Module/names.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

 #  next(csv_reader)  # Skip the header row
    with open("CSV_Module/new_names.csv", "w") as new_file:
        csv_writer =  csv.writer(new_file, delimiter="-")
        for line in csv_reader:
            csv_writer.writerow(line)
    # for line in csv_reader:
    #     print(line) 
