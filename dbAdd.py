import sqlite3


def main(go = False):
    if go == True:
        addEntry()


def addEntry():
    answers = getInputs()
    filename = "storeDB.sqlite"
    table1 = "products"
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    try:
        connCursor.execute("INSERT OR IGNORE INTO {tn} VALUES (NULL, {f1}, {f2}, {f3}, {f4}, {f5}, {f6})".
                   format(tn=table1, f1="\'" + answers[0] + "\'", f2=float(answers[1]), f3=int(answers[2]),
                  f4=int(answers[3]), f5="\'" + answers[4] + "\'", f6="\'" + answers[5] + "\'"))
    except sqlite3.IntegrityError:
        print("Error with primary key")
    except sqlite3.Error:
        print("Error; bad values or no table")

    conn.commit()
    conn.close()


def getInputs():
    prodName = input("Product Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    numSold = input("# Sold: ")
    description = input("Description: ")
    color = input("Color: ")
    answers = [prodName, price, quantity, numSold, description, color]
    return answers

# main()
