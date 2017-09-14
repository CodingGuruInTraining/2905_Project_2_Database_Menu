import sqlite3

# Defines main.
def main(go = False):
    if go == True:
        allData = queryAll()
        showData(allData)


def queryAll():
    # Variables are defined.
    filename = "storeDB.sqlite"
    table1 = "products"

    # Connects to database.
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    try:
        # Combines statement string and retrieves results.
        connCursor.execute('SELECT * FROM {tn}'.format(tn=table1))
        allData = connCursor.fetchall()
    except sqlite3.Error:
        print("can't find table")

    # Closes connection and returns data.
    conn.close()
    return allData


def showData(allData):
    # Sets column lengths.
    formatStr = "%-10s%-15s%-10s%-10s%-10s%-30s%-15s"
    # Displays headers.
    print(formatStr % ("prodID", "Name", "Price", "Quantity", "NumSold", "Description", "Color"))
    # Loops through and prints data.
    for row in allData:
        print(formatStr % (str(row[0]), row[1], "$" + str(row[2]), str(row[3]), str(row[4]), row[5], row[6]))


# Helpful reference:
    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
