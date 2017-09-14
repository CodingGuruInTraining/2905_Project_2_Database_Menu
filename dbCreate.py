import sqlite3


def main():
    createTable()


def createTable():
    filename = "storeDB.sqlite"
    table1 = "products"
    idField = "prodID"
    field1 = "Name"
    field2 = "Price"
    field3 = "Quantity"
    field4 = "NumSold"
    field5 = "Description"
    field6 = "Color"

    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    connCursor.execute('CREATE TABLE {tn} ({f0} INTEGER PRIMARY KEY, {f1} TEXT NOT NULL, {f2} REAL, {f3} INTEGER, {f4} INTEGER, {f5} TEXT, {f6} TEXT)'\
                       .format(tn=table1, f0=idField, f1=field1, f2=field2, f3=field3, f4=field4, f5=field5, f6=field6))

    conn.commit()
    conn.close()

main()
