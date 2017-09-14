import sqlite3


def main(go = False):
    if go == True:
        updateEntry()


def updateEntry():
    filename = "storeDB.sqlite"
    table1 = "products"
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    try:
        connCursor.execute("UPDATE {tn} SET")
    except sqlite3.Error:
        print("Error")

    conn.commit()
    conn.close()


# main()
