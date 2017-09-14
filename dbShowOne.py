import sqlite3


def main(go = False):
    if go == True:
        queryOne()


def queryOne():
    filename = "storedb.sqlite"
    table1 = "products"
    idField = "prodID"

    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    showValue = int(input("Enter the Product ID for the product you want to show:"))
    try:
        connCursor.execute("SELECT * FROM {tn} WHERE {c1}={v1}".format(tn=table1, c1=idField, v1=showValue))
    except sqlite3.Error:
        print("Error")
    oneData = connCursor.fetchone()
    print(oneData)
    conn.close()

main()