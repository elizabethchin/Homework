files = {"um-deliveries-20140519.txt" : "Day 1", 
"um-deliveries-20140520.txt" : "Day 2",
 "um-deliveries-20140521.txt" : "Day 3"}

day = "1"
file = "um-deliveries-20140519.txt"
def melon_delivery_report(files):
        print("Day " + day)
        the_file = open(file)
        for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                melon = words[0]
                count = words[1]
                amount = words[2]

                print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
        the_file.close()

print(melon_delivery_report(day, file))
