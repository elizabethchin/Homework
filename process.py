log_file = open("um-server-01.txt")
#opens text file

def sales_reports(log_file):
    for line in log_file:
        #loops through each line in file
        line = line.rstrip()
        #removes leading whitespace
        day = line[0:3]
        #keeps the first three index
        if day == "Mon":
        #if day equals to Monday it prints
            print(line)


sales_reports(log_file)
