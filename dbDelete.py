import sqlite3


def main(go = False):
    if go == True:
        deleteEntry()

def deleteEntry():
    filename = "storeDB.sqlite"
    table1 = "products"
    idField = "prodID"

    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    deleteValue = int(input("Enter the Product ID for the product you want to remove:"))

    try:
        connCursor.execute("DELETE FROM {tn} WHERE {c1}={v1}".format(tn=table1, c1=idField, v1=deleteValue))
    except sqlite3.Error:
        print("something isn't right here")

    conn.commit()
    conn.close()

# main()
