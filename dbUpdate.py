import sqlite3


def main():
    updateEntry()


def updateEntry():
    filename = "storeDB.sqlite"
    table1 = "products"
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()


    connCursor.execute("UPDATE {tn} SET")

    conn.commit()
    conn.close()


main()
