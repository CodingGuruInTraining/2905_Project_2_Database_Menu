import sqlite3

# Defines main.
def main(go = False):
    if go == True:
        deleteEntry()

def deleteEntry():
    # Variables are defined.
    filename = "storeDB.sqlite"
    table1 = "products"
    idField = "prodID"

    # Connects to database.
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()


    # Exception handler.
    try:
        # Gets input from user and converts to int.
        deleteValue = int(input("Enter the Product ID for the product you want to remove:"))
        # Combines statement string.
        connCursor.execute("DELETE FROM {tn} WHERE {c1}={v1}".format(tn=table1, c1=idField, v1=deleteValue))
    except sqlite3.Error:
        print("something isn't right here; you sure you have an int entered?")

    # Executes statement and closes connection.
    conn.commit()
    conn.close()

