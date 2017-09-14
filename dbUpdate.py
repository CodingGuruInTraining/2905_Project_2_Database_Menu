import sqlite3


def main(go = False):
    if go == True:
        updateEntry()


def updateEntry():
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
    prodid = int(input("Enter product id of product to update:"))
    newData = getInputs()

    try:
        connCursor.execute("UPDATE {tn} SET {c1}={v1}, {c2}={v2}, {c3}={v3}, {c4}={v4}, {c5}={v5},\
            {c6}={v6} WHERE {id}={v7}".format(tn=table1, c1=field1, v1=newData[0], c2=field2, \
            v2=float(newData[1]), c3=field3, v3=int(newData[2]), c4=field4, v4=int(newData[3]), \
            c5=field5, v5=newData[4], c6=field6, v6=newData[5], id=idField, v7=prodid))
    except sqlite3.Error:
        print("Error")

    conn.commit()
    conn.close()


def getInputs():
    name = input("Enter new name:")
    price = input("Enter new price:")
    quantity = input("Enter new quantity:")
    numsold = input("Enter new number sold:")
    descript = input("Enter new description:")
    color = input("Enter new color:")

    return [name, price, quantity, numsold, descript, color]
