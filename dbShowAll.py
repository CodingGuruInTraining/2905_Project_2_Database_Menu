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
    print("%-10s%-15s%-10s%-10s%-10s%-30s%-15s" % ("prodID", "Name", "Price", "Quantity", "NumSold", "Description", "Color"))
    print("%-15s" * 7 % (
    "prodID", "Name", "Price", "Quantity", "NumSold", "Description", "Color"))
    # for row in allData:


main()
