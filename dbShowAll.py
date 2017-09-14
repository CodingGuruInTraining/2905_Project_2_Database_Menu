import sqlite3


def main():
    allData = queryAll()
    showData(allData)
    # return allData


def queryAll():
    filename = "storeDB.sqlite"
    table1 = "products"

    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    connCursor.execute('SELECT * FROM {tn}'.format(tn=table1))
    allData = connCursor.fetchall()

    conn.close()
    return allData


def showData(allData):
    formatStr = "%-10s%-15s%-10s%-10s%-10s%-30s%-15s"
    print(formatStr % ("prodID", "Name", "Price", "Quantity", "NumSold", "Description", "Color"))
    for row in allData:
        print(formatStr % (str(row[0]), row[1], "$" + str(row[2]), str(row[3]), str(row[4]), row[5], row[6]))

main()


# Helpful reference:
    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
