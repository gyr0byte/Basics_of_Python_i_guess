import csv
path = "CSV_Module/names.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line) # this is to access all the values
    # for line in csv_reader:   # reading all the values
    #     print(line["email"])  # accessing just the emails
    with open("CSV_Module/new_names.csv", "w") as new_file:
        field_names = ["first_name", "last_name", "email"]
        csv_writer =  csv.DictWriter(new_file, fieldnames=field_names)
        
        csv_writer.writeheader()
        for line in csv_reader:
            # del line["email"] # to delete email while writing
            csv_writer.writerow(line)
