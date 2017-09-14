import sqlite3

# Defines main.
def main(go = False):
    if go == True:
        queryOne()


def queryOne():
    # Variables are defined.
    filename = "storedb.sqlite"
    table1 = "products"
    idField = "prodID"

    # Connects to database.
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    # Exception handler.
    try:
        # Gets input from user and converts to int.
        showValue = int(input("Enter the Product ID for the product you want to show:"))
        connCursor.execute("SELECT * FROM {tn} WHERE {c1}={v1}".format(tn=table1, c1=idField, v1=showValue))
    except sqlite3.Error:
        print("Error")

    oneData = connCursor.fetchone()
    print(oneData)

    conn.close()
#
# main()