import csv
# list
field_names = ["Name", "Author", "Publisher", "Price"]
# dictionary
book1 = {"Name": "Computer programming, part 1", "Author": "Tamim shaharir subeen", "Publisher": "dimik prokashoni", "Price": "240.00"}
book2 = {"Name": "Computer programming, part 2", "Author": "Tamim shaharir subeen", "Publisher": "dimik prokashoni", "Price": "230.00"}
book3 = {"Name": "Learn Programming with python", "Author": "Tamim sharharir subeen", "publisher": "Dimik prokashoni", "price": "200.00"}
# list
book_list = [book1, book2, book3]
# writing csv
with open("book_list.csv", "w") as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)
print("alhamdulillah")